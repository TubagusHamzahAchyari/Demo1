from django.urls import path
from .views import capture_image,camera_image_change

urlpatterns = [
    path('capture/', capture_image, name='capture_image'),
    path('image/change/<int:image_id>/', camera_image_change, name='camera_image_change'),

]