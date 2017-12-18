from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/', views.category, name='category'),
    url(r'^photo/', views.photo, name='photo'),
    url(r'^item_detail/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
