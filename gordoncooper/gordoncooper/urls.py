from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from gordoncooper.views import ListView, PostView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gordoncooper.views.home', name='home'),
    # url(r'^gordoncooper/', include('gordoncooper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ListView.as_view(),
        {'type': None}, name='home'),
    url(r'^downloads$', ListView.as_view(),
        {'type': 'download'}, name='downloads'),
    url(r'^diary$', ListView.as_view(),
        {'type': 'diary'}, name='diary'),
    url(r'^gallery$', ListView.as_view(),
        {'type': 'gallery'}, name='gallery'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'),
        {'menu': 'contact'}, name='contact'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        PostView.as_view(), name='post-detail'),

    #(r'^test-bootstrap$', TemplateView.as_view(template_name='test-bootstrap.html')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
