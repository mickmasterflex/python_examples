from django.conf.urls import *
from accounts import views

userprofileurls = patterns('accounts.views',
    # Index page
    url('^$', views.ListUsersView.as_view(), name='index'),
    url(r'^(?P<username>[\w\d\-\.]+)/edit/$', 
        views.EditUserView.as_view(), name='edit'),
    url(r'^(?P<username>[\w\d\-\.]+)/toggle_enabled/$',
        'toggle_enabled', name='toggle_enabled'),
    url(r'^(?P<username>[\w\d\-\.]+)password/$', 
        views.UpdatePasswordView.as_view(), name="edit_password"),
)

urlpatterns = patterns('accounts.views',
    url(r'^user-profile/', include(userprofileurls, namespace="user_profile")),
    url(r'^my-user-profile/$', views.EditMyUserView.as_view(),
        name='edit_my_profile'),
    url(r'my-user-profile/edit-password/$', 
        views.UpdateMyPasswordView.as_view(), name="edit_my_password"),
    url('^login/$', 'login', name='login'),
    url('^logout/$', 'logout', name='logout'),
)

