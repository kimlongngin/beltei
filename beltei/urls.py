from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include
from django.apps import apps
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.conf.urls.i18n import i18n_patterns

from django.utils.translation import gettext_lazy as _ 
"""
    Check data for uploading
"""
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'Beltei'
admin.site.site_header = "Beltei Admin"
admin.site.site_title = "Beltei Admin Portal"
admin.site.index_title = "Welcome to beltei student portal"

# urlpatterns = [
# 	path('i18n/', include('django.conf.urls.i18n')),
# 	path('admin/', admin.site.urls),
# 	path('', include('students.urls')),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
	path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
	path('admin/', admin.site.urls),
	path('', include('students.urls')),
	prefix_default_language = True, 
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)