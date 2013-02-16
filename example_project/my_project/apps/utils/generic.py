from __future__ import unicode_literals

from django.core import exceptions
from django.views import generic
from django import http


class CreateUpdateView(generic.UpdateView):
    """
        CreateUpdateView is the same as Django's generic.UpdateView, except it
        doesn't complain if there is no <pk> or <slug> set in the url,
        allowing you to use one view for both creating and updating objects
    """
    # overridable
    created_display = 'Created'
    saved_display = 'Saved'

    def __init__(self, *args, **kwargs):
        self.is_editing = False

        super(CreateUpdateView, self).__init__(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.

        """
        # Use a custom queryset if provided; this is required for subclasses
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        elif slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # if none are set, this is a create view, so return none
        else:
            return None

        # if we got this far, we are editing an object, not creating one
        self.is_editing = True

        try:
            obj = queryset.get()
        except exceptions.ObjectDoesNotExist:
            raise http.Http404(
                'No {0} found matching the query'.format(
                    queryset.model._meta.verbose_name))
        return obj

    def get_context_data(self, **kwargs):
        """
            Extends the UpdateView, adding "is_editing".

            "is_editing" will be True if <pk> and <slug> were passed in
            via the url.
        """
        context = super(CreateUpdateView, self).get_context_data(**kwargs)
        context['is_editing'] = self.is_editing
        return context

    @property
    def save_type_display(self):
        """
            Returns the save type display, for example, "Saved" if this is an
            edit view, and "Created" if it is a create view
        """
        return self.saved_display if self.is_editing else self.created_display
