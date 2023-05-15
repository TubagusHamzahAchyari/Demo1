import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image

def capture_image(request):
    # Ambil gambar dari kamera
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()
    camera.release()

    # Konversi gambar menjadi format yang dapat disimpan oleh Django
    _, image_buffer = cv2.imencode('.jpg', frame)
    image_data = np.array(image_buffer).tobytes()

    # Simpan gambar ke model Image
    image = Image.objects.create()
    image.image.save('image.jpg', ContentFile(image_data))
    image.save()

    return redirect('admin:camera_image_change', image.id)


def camera_image_change(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        # Lakukan pemrosesan form jika diperlukan
        pass

    context = {
        'image': image,
    }

    return render(request, 'camera/image_change.html', context)
