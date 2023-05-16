# import cv2
# import numpy as np
# from django.core.files.base import ContentFile
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Image
#
#
#
#
# def camera_image_change(request, image_id):
#     image = get_object_or_404(Image, id=image_id)
#
#     if request.method == 'POST':
#         # Lakukan pemrosesan form jika diperlukan
#         pass
#
#     context = {
#         'image': image,
#     }
#
#     return render(request, 'camera/image_change.html', context)
#
# def capture_image(request):
#     # Ambil gambar dari kamera
#     camera = cv2.VideoCapture(0)
#     _, frame = camera.read()
#     camera.release()
#
#     # Konversi gambar menjadi format yang dapat disimpan oleh Django
#     _, image_buffer = cv2.imencode('.jpg', frame)
#     image_data = np.array(image_buffer).tobytes()
#
#     # Simpan gambar ke model Image
#     image = Image.objects.create()
#     image.image.save('image.jpg', ContentFile(image_data))
#     image.save()
#
#     return redirect('admin:camera_image_change', image.id)

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'app1.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')