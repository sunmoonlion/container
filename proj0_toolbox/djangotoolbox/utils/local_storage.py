# utils/local_storage.py

from django.core.files.storage import FileSystemStorage

class LocalStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = '/path/to/local/media/'
        kwargs['base_url'] = '/media/'
        super().__init__(*args, **kwargs)
