from django.core.files.storage import default_storage
from django.http import HttpRequest
from .interfaces import ImageStorage
from django.conf import settings



class ImageLocalStorage(ImageStorage):
    def store(self, request: HttpRequest):
        profile_image = request.FILES.get('profile_image', None)
        if profile_image:
            file_name = default_storage.save('uploaded_images/' + profile_image.name, profile_image)
            return settings.MEDIA_URL + file_name
        return None