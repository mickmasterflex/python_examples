from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from django.conf import settings
from django.views.generic.edit import FormView

from accounts import constants
from accounts import mixins as accounts_mixins
from accounts.forms import UserForm, MyUserForm

from common import utils
from common import constants as common_constants
from common.generic import CreateUpdateView

def login(request):
    """
    This displays the login page and lets the user login.
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('ses_index'))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Now that we have the required values lets proceed to validation
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if not request.POST.get('remember'):
                    request.session.set_expiry(0)
                auth.login(request, user)
                return HttpResponseRedirect(reverse('ses_index'))
            else:
                messages.error(request, _('Your account is not active'))
        else:
            messages.error(request, _('Invalid username or password'))

    return render(request, 'login.html', {})

def logout(request):
    """
    Log the user out and take them to the login page.
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('ses_index'))

class ListUsersView(accounts_mixins.LoginRequiredMixin,
                    accounts_mixins.PermissionsRequiredMixin, ListView):
    permissions_required = constants.PERMISSIONS_SES_STAFF_AND_ABOVE
    template_name = 'accounts/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(ListUsersView, self).get_context_data(**kwargs)
        context['showall'] = self.request.GET.get('showall', '')
        context['letters'] = utils.first_letters(self.object_list,
                'first_name')
        return context

    def get_queryset(self):
        showall = self.request.GET.get('showall', '')
        users = User.objects.all().order_by('username')
        if not showall:
            users = users.filter(is_active=True)

        self.sublist = False
        letter = self.request.GET.get('letter')
        if letter:
            self.sublist = True
            if letter == '#':
                users = users.filter(first_name__regex='^\d')
            elif letter == 'all':
                pass
            else:
                users = users.filter(first_name__istartswith=letter)

        query = self.request.GET.get('query')
        if query:
            self.sublist = True
            users = users.filter(Q(username__icontains=query) |
                    Q(last_name__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(email__icontains=query))

        return users

class EditUserView(accounts_mixins.LoginRequiredMixin,
                   accounts_mixins.PermissionsRequiredMixin, CreateUpdateView):
    permissions_required = constants.PERMISSIONS_SES_STAFF_AND_ABOVE
    template_name = 'accounts/edit.html'
    form_class = UserForm
    model = User

    def get_object(self, *args, **kwargs):
        user = None
        if 'username' in self.kwargs:
            user = get_object_or_404(User,
                username__iexact=self.kwargs['username'])
            self.is_editing = True

        return user

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = super(EditUserView, self).get_form_kwargs()

        if self.is_editing:
            kwargs.update({'initial': {
                'access_level': self.object.profile.permission}})

        else:
            kwargs.update({'initial': {
                'access_level': constants.PERMISSION_USER}})

        return kwargs

    def form_valid(self, form):
        response = super(EditUserView, self).form_valid(form)

        if not self.is_editing:
            self.send_email()
            messages.success(self.request,
                _('You\'ve added {0}'.format(self.object.username)))
        else:
            messages.success(self.request,
                _('You\'ve updated {0}'.format(self.object.username)))

        return response

    def get_success_url(self):
        return reverse('accounts:user_profile:index')

    def send_email(self):
        password = utils.generate_random_value(
                common_constants.LENGTH_OF_PASSWORD)
        self.object.set_password(password)
        self.object.save()

        current_site = Site.objects.get_current()
        subject = render_to_string(
                "accounts/new_user_email-subject.txt", {
                    'site': current_site,
                }
        )
        message = render_to_string(
                "accounts/new_user_email-body.txt", {
                    'site': current_site,
                    'request': self.request,
                    'user': self.object,
                    'password': password,
                }
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
            [self.object.email,])

class EditMyUserView(accounts_mixins.LoginRequiredMixin, CreateUpdateView):
    template_name = 'accounts/edit_my_profile.html'
    form_class = MyUserForm
    model = User

    def get_object(self, *args, **kwargs):
        return self.request.user

    def form_valid(self, form):
        super(EditMyUserView, self).form_valid(form)
        messages.success(self.request,
            _("You've updated {0}'s account".format(self.object.username)))

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:edit_my_profile')

class UpdatePasswordView(accounts_mixins.LoginRequiredMixin,
                         accounts_mixins.PermissionsRequiredMixin, FormView):
    permissions_required = constants.PERMISSIONS_SES_STAFF_AND_ABOVE
    template_name = 'accounts/edit_password.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request,
            _('Successfully changed password'))
        return super(UpdatePasswordView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,
            _('There was an error updating your password.'))
        return super(UpdatePasswordView, self).form_invalid(form)

    def get_success_url(self):
        return render(self.request, 'accounts/password_save_success.html')

    def get_form_kwargs(self):
        #kwargs = dict()
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = User.objects.get(
            username__iexact=self.kwargs['username'])
        return kwargs

class UpdateMyPasswordView(accounts_mixins.LoginRequiredMixin, FormView):
    template_name = 'accounts/edit_my_password.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request,
            _("Successfully changed password"))
        return render(self.request, 'accounts/password_save_success.html')

    def form_invalid(self, form):
        messages.error(self.request,
            _("There was an error updating your password."))
        return super(UpdateMyPasswordView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('accounts:edit_my_profile')

    def get_form_kwargs(self):
        kwargs = super(UpdateMyPasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

@login_required
@accounts_mixins.permissions_required(
    constants.PERMISSIONS_SES_STAFF_AND_ABOVE)
def toggle_enabled(request, username):
    user = get_object_or_404(User, username=username)

    msg = 'Enabled' if not user.is_active else 'Disabled'

    user.is_active = not user.is_active
    user.save()

    messages.success(request, _('User has been {0}'.format(msg)))

    return HttpResponseRedirect(reverse('accounts:user_profile:index'))

def index(request):
    return render(request, 'index.html')
