from django.urls import path
from .views import Home

urlpatterns = [
    # path('capture/', capture_image, name='capture_image'),
    # path('camera/capture/', camera_image_change, name='camera_image_change'),
    # path('image/change/<int:image_id>/', camera_image_change, name='camera_image_change'),
    path ('home', Home, name='Home')
]