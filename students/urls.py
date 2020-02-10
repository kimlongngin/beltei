from django.conf.urls import include, url
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

from .views import SearchStudentView


app_name = 'students'


urlpatterns = [
	path('search/', SearchStudentView.as_view(), name='student_search'),

    url(r'^$', views.IndexView.as_view(), name='index_view'),    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)