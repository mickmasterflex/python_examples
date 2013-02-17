from django.contrib.auth.models import User
from django.views.generic import ListView

from accounts import constants as account_constants
from accounts import mixins as accounts_mixins

class ScoreListView(accounts_mixins.LoginRequiredMixin,
                    accounts_mixins.PermissionsRequiredMixin, ListView):
    permissions_required = account_constants.PERMISSIONS_USER
    template_name = 'bowling/scores.html'
    model = User


