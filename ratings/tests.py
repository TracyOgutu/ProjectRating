from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        creating a foreign key instance
        '''
        self.newuser=User(username='johnny')
        self.newuser.save()

        self.biography=Profile(profile_photo='pic.jpg',bio='treats',contact='0782345678',editor=self.newuser)

    def test_instance(self):
        '''
        Testing the self instance
        '''
        self.assertTrue(isinstance(self.biography,Profile))

    def test_save_profile(self):
        '''
        Testing save profile function
        '''
        self.biography.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        '''
        Testing delete profile function
        '''
        self.biography.save_profile()
        self.biography.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    def test_get_profile(self):
        '''
        Testing profile retrieval
        '''
        self.biography.save_profile()
        firstprofile=Profile.get_profile()
        self.assertTrue(firstprofile is not None)

class ProjectTestClass(TestCase):

    def setUp(self):
        '''
        creating a user foreign key instance
        '''
        self.newuser=User(username='johnny') 
        '''
        saving the foreign key instance
        '''
        self.newuser.save()

        '''
        creating the Project class instance and including foreign key references
        '''

        self.projects=Project(title='jupiter',image='img.jpg',description='whatamarvel',editor=self.newuser)

    def test_instance(self):
        '''
        Testing the Project instance
        '''
        self.assertTrue(isinstance(self.projects,Project))

    def test_save_project(self):
        '''
        Testing the save project function
        '''
        self.projects.save_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)>0)

    def test_delete_project(self):
        '''
        Testing the delete project function
        '''
        self.projects.save_project()
        self.projects.delete_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)==0)

    def test_get_images(self):
        '''
        Testing project retrieval
        '''
        self.projects.save_project()
        firstproject=Project.get_projects()
        self.assertTrue(firstproject is not None)