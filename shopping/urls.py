from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/', views.category, name='category'),
    url(r'^photo/', views.photo, name='photo'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^category/cpu', views.category_cpu, name='category_cpu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
