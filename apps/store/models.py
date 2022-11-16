from django.db import models
from io import BytesIO
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # slug = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_new = models.BooleanField(default=False)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ('-date_added',)

    # def save(self):
    #     super().save()  # saving image first
    #
    #     img = Image.open(self.image.path)  # Open image using self
    #
    #     if img.height > 392 or img.width > 392:
    #         new_img = (392, 400)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()
    #
    #             return self.thumbnail.url
    #         else:
    #             return 'https://via.placeholder.com/240*180.jpg'
    #
    # def make_thumbnail(self, image, size=(345, 400)):
    #     img = Image.open(image)
    #     if img.mode in ("RGBA", "P"):
    #         img = img.convert("RGB")
    #     # img.convert('RGB')
    #     img.thumbnail(size)
    #
    #     thumb_io = BytesIO()
    #     img.save(thumb_io,'JPEG',quality=85)
    #
    #     thumbnail = File(thumb_io, name=image.name)
    #
    #     return thumbnail