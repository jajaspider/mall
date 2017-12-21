from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/', views.category, name='category'),
    url(r'^photo/', views.photo, name='photo'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^cpu/', views.category_cpu, name='category_cpu'),
    url(r'^ram/', views.category_ram, name='category_ram'),
    url(r'^mb/', views.category_mb, name='category_mb'),
    url(r'^vga/', views.category_vga, name='category_vga'),
    url(r'^ssdhdd/', views.category_ssdhdd, name='category_ssdhdd'),
    url(r'^case/', views.category_case, name='category_case'),
    url(r'^power/', views.category_power, name='category_power'),
    url(r'^inputdevices/', views.category_inputdevices, name='category_inputdevices'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
