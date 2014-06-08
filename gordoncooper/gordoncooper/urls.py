from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from gordoncooper.views import Home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gordoncooper.views.home', name='home'),
    # url(r'^gordoncooper/', include('gordoncooper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^$', TemplateView.as_view(template_name='about.html')),
    url(r'^$', Home.as_view(), name='home'),
    (r'^test-bootstrap$', TemplateView.as_view(template_name='test-bootstrap.html')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
