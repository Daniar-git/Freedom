from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


class Service:
    
    def upload_avatar(self, request_file):
        upload_result = upload(request_file)
        url, _ = cloudinary_url(
            upload_result['public_id'],
            format='jpg',
            crop='fill',
            width=300,  # noqa: WPS432
            height=300,  # noqa: WPS432
        )
        return url