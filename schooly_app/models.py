from django.db import models
from django.contrib.auth.models import User

class ClassRoom(models.Model):
	name = models.CharField(max_length=50)
	students = models.ManyToManyField(User)

class Post(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)
    classroom = models.ForeignKey(ClassRoom)

'''Can be used for extension later'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])