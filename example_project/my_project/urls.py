from django.conf.urls import patterns, include, url
from django.conf import settings

# for static front end templates
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # login url
    url(r'^$', 'accounts.views.index', name='ses_index'),

    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^common/', include('common.urls', namespace='common')),
    url(r'^bowling/', include('bowling.urls', namespace='bowling')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

if settings.TEMPLATE_DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'serve', {
            'show_indexes': True,
            'document_root': settings.STATIC_ROOT}),
    )

