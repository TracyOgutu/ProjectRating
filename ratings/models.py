from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    '''
    Class that contains User Profile details
    '''
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    contact=models.IntegerField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
   

    def __str__(self):
        '''
        Setting up self 
        '''
        return self.bio

    @classmethod
    def get_profile(cls):
        '''
        Method to retrieve the profile details
        '''
        profile=cls.objects.all()
        return profile

    def save_profile(self):
        '''
        Method to save the created profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Method to delete the profile
        '''
        self.delete()

class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/',blank=True)
    description=HTMLField()
    link=models.URLField( max_length=128, db_index=True,unique=True,blank=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)

