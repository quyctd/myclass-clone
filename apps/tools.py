#upload image to cloudinary
import cloudinary
from cloudinary import uploader

#cloudinary config
cloudinary.config(
    cloud_name="flask-image",
    api_key='133444264233997',  
    api_secret = 'SrlSO-4T4W2lQx72PEYGHSEnOwU'
)

def pre_upload_cover_course(sender, instance, *args, **kwargs):
    if instance.anh_cover:
        try:
                cover_photo = instance.anh_cover.open()
                cloud_img = uploader.upload(cover_photo)
                cloud_link = cloud_img['url']
                instance.cover_link = cloud_link
        except:
                print("Course cover file not found!")
                return

def pre_upload_avatar_image(sender, instance, *args, **kwargs):
    if instance.avatar:
        try:
                avatar = instance.avatar.open()
                cloud_avatar = uploader.upload(avatar)
                cloud_link = cloud_avatar['url']
                instance.avatar_link = cloud_link
        except:
                print("Avatar file not found!")
                return