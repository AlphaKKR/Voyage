from django.db import models
import os

def get_image_path_cover(instance, filename):
    return os.path.join('Cover', str(instance.room_id), filename)

def get_image_path_img(instance, filename):
    return os.path.join('Img', str(instance.room_id), filename)

class Room(models.Model):
    room_id         = models.AutoField(primary_key=True, default=0)
    price           = models.IntegerField(default=0, null=False)
    details         = models.CharField(max_length=100, default='', null=False)
    room_desc       = models.TextField(max_length=1000, default='', null=False)
    cover_image     = models.ImageField(upload_to=get_image_path_cover, blank=True, null=True)
    image_1         = models.ImageField(upload_to=get_image_path_img, blank=True, null=True)
    image_2         = models.ImageField(upload_to=get_image_path_img, blank=True, null=True)
    image_3         = models.ImageField(upload_to=get_image_path_img, blank=True, null=True)
    image_4         = models.ImageField(upload_to=get_image_path_img, blank=True, null=True)

    def __str__(self):
        return (str(self.room_id) + " -- " + str(self.details))