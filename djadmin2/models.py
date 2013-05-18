"""

For wont of a better name, this module is called 'models'. It's role is
synonymous with the django.contrib.admin.sites model.

"""

<<<<<<< Updated upstream
=======
from djadmin2 import apiviews
from djadmin2 import views
>>>>>>> Stashed changes

try:
    import floppyforms as forms
except ImportError:
    from django import forms


class BaseAdmin2(object):

    search_fields = []

    # Show the fields to be displayed as columns
    # TODO: Confirm that this is what the Django admin uses
    list_fields = []

    #This shows up on the DocumentListView of the Posts
    list_actions = []

    # This shows up in the DocumentDetailView of the Posts.
    document_actions = []

    # shows up on a particular field
    field_actions = {}

    fields = None
    exclude = None
    fieldsets = None
    form = forms.ModelForm
    filter_vertical = ()
    filter_horizontal = ()
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ()
    ordering = None

    def has_view_permission(self, request):
        """
        Returns True if the given HttpRequest has permission to view
        *at least one* page in the mongonaut site.
        """
        return request.user.is_authenticated() and request.user.is_active

    def has_edit_permission(self, request):
        """ Can edit this object """
        return request.user.is_authenticated() and request.user.is_active and request.user.is_staff

    def has_add_permission(self, request):
        """ Can add this object """
        return request.user.is_authenticated() and request.user.is_active and request.user.is_staff

    def has_delete_permission(self, request):
        """ Can delete this object """
        return request.user.is_authenticated() and request.user.is_active and request.user.is_superuser


class Admin2(BaseAdmin2):

    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    save_as = False
    save_on_top = False
<<<<<<< Updated upstream
=======

    #  Views
    index_view = views.ModelListView
    create_view = views.ModelAddFormView
    update_view = views.ModelEditFormView
    detail_view = views.ModelDetailView
    delete_view = views.ModelDeleteView

    api_index_view = apiviews.ModelListCreateAPIView

    def __init__(self, model, **kwargs):
        self.model = model

    def get_urls(self):
        return patterns('',
            url(
                regex=r'^$',
                view=self.index_view.as_view(model=self.model),
                name='index'
            ),
            url(
                regex=r'^create/$', 
                view=self.create_view.as_view(model=self.model), 
                name='create'
            ),
            url(
                regex=r'^(?P<pk>[0-9]+)/$',
                view=self.detail_view.as_view(model=self.model), 
                name='detail'
            ),
            url(
                regex=r'^(?P<pk>[0-9]+)/update/$',
                view=self.update_view.as_view(model=self.model),
                name='update'
            ),
            url(
                regex=r'^(?P<pk>[0-9]+)/delete/$',
                view=self.delete_view.as_view(model=self.model),
                name='delete'
            ),
        )

    def get_api_urls(self):
        return patterns('',
            url(
                regex=r'^$',
                view=self.api_index_view.as_view(model=self.model),
                name='api-index'
            ),
        )

    @property
    def urls(self):
        # We set the application and instance namespace here
        return self.get_urls(), None, None

    @property
    def api_urls(self):
        # We set the application and instance namespace here
        return self.get_api_urls(), None, None
>>>>>>> Stashed changes
