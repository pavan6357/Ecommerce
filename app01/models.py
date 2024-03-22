from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null= True)
    designation = models.CharField(max_length=100, null= True)
    mobile_number = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(null=True, upload_to='static/images/' )
    profile_summary = models.TextField(max_length=300, null= True)
    city = models.CharField(max_length=100, null= True)
    state = models.CharField(max_length=100, null= True)
    country = models.CharField(max_length=100, null= True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self): # this allows us to see the product in Django admin when we look at it
        return self.title 
    

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])


class Product(models.Model):
    product_name = models.CharField(max_length=200, null= True)
    product_description = models.CharField(max_length=1000, null= True)
    no_product_orders = models.PositiveIntegerField(null= True)
    product_rating = models.PositiveSmallIntegerField(null= True)
    product_image = models.URLField(null=True)

    def __str__(self):
        return self.product_name