from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import hashlib

class ClassRoom(models.Model):
	course = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	students = models.ManyToManyField(User,related_name="class_participants")
	code = models.CharField(max_length=256)

	#Very important to call this function after creating a ClassRoom
	def create_code(self):
		self.code = hashlib.md5(self.course+self.name).hexdigest()

class Post(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)
    classroom = models.ForeignKey(ClassRoom,related_name='posts_in_class')

'''Can be used for extension later'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])