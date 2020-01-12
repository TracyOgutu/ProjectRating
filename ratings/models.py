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
    contact=models.CharField(max_length=25)
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

    @classmethod
    def single_profile(cls,user_id):
        '''
        function gets a single profile posted by id
        '''
        profile=cls.objects.filter(editor=user_id)
        return profile

    @classmethod
    def get_profilepic_id(cls,imageId):
        '''
        function that gets a profilepic id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id

class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/',blank=True)
    description=HTMLField()
    link=models.URLField( max_length=128, db_index=True,unique=True,blank=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.title

    def save_project(self):
        '''
        Method for saving the project
        '''
        self.save()

    def delete_project(self):
        '''
        Method for deleting the project
        '''
        self.delete()
    
    @classmethod
    def get_projects(cls):
        '''
        Method for retrieving all images
        '''
        project=cls.objects.all()
        return project

    @classmethod
    def user_projects(cls,user_id):
        '''
        function gets projects posted by id
        '''
        project_posted=cls.objects.get(editor=user_id)
        return project_posted    

    @classmethod
    def search_by_title(cls,tag):
        '''
        Method for searching for a project using the title
        '''

        search_result=cls.objects.filter(title__icontains=tag)
        return search_result

    @classmethod
    def single_project(cls,project_id):
        '''
        function gets a single project posted by id
        '''
        project_posted=cls.objects.get(id=project_id)
        return project_posted

    @classmethod
    def get_image_id(cls,imageId):
        '''
        function that gets an image id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id

