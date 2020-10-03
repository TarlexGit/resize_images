from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 


urlpatterns = [
    path('', views.GetImages.as_view(), name='list_images'),
    path('image/<int:pk>/',  views.ImageDetail.as_view(),  name='model-detail-view'),
    path('add/', views.add_image, name='add_image'),
    path('both/', views.except_both, name='both'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)