
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    userid = models.CharField(max_length=50, primary_key=True)  
    mobil_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ["mobil_no"]  

    def __str__(self):
        return self.email



class UserProfile(models.Model):  
    userid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_name = models.CharField(max_length=200)
    profile_img = models.ImageField(null=True, upload_to='profileimg/', default="avatar.svg")
    mobile_no = models.CharField(max_length=15, unique=True)  # Ensure it can be used as a ForeignKey
    business_type = models.CharField(max_length=15)  
    owner_name = models.CharField(max_length=100, null=True)
    total_room = models.PositiveIntegerField()  
    room_rent = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.profile_name



class Location(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobil_no = models.ForeignKey(UserProfile, to_field='mobile_no', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.userid.email} - {self.location}"
