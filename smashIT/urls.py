
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from convert.sitemap import CustomSitemap

from django.views.generic.base import TemplateView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


# sitemaps = {
#     'custom': CustomSitemap,
# }


handler404 = 'convert.views.custom_page_not_found_view'
handler500 = 'convert.views.custom_error_view'
handler403 = 'convert.views.custom_permission_denied_view'
handler400 = 'convert.views.custom_bad_request_view'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('convert.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('static/icon/favicon.ico')))
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
