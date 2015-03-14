from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='/expression/')),
                       url(r'^expression/', include('expression.urls')),
                       ) + static(settings.MEDIA_URL,
                                  document_root=settings.MEDIA_ROOT)+ \
                         static(settings.STATIC_URL)
