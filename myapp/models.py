from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    image = models.ImageField(default='default.png',null=True,blank=True)
    
    def __str__(self):
        return str(self.user)

# creating a reciver signals for sender User
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# connecting the sender and reciver
post_save.connect(create_profile,sender=User)

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.TextField()

    def __str__(self):
        return str(self.author)