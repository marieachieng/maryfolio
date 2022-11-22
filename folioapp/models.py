from django.db import models

# BLOG
class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post_img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


# BIO DATA
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=13)
    location = models.TextField(max_length=100)
    about_me = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='images/')

class Job(models.Model):
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length = 200, null=True)
    started_at = models.DateField()
    ended_at = models.DateField()
    is_ended = models.BooleanField()
    role = models.CharField(max_length=200)
    role_description = models.TextField(blank=True)

class Socialaccount(models.Model):
    social_url = models.URLField(max_length = 200, null=True)
    social_name = models.CharField(max_length=45)
    is_public = models.BooleanField()

class Education(models.Model):
    course_name = models.CharField(max_length=250)
    institute_name = models.CharField(max_length=250)
    institute_url = models.URLField(max_length = 200, null=True)
    description = models.TextField(blank=True)
    started_at = models.DateField()
    ended_at = models.DateField()
    is_completed = models.BooleanField()

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_img = models.ImageField(upload_to='images/')
    is_public = models.BooleanField()

class Certification(models.Model):
    certificate_name = models.CharField(max_length=150)
    certificate_img = models.ImageField(upload_to='images/')
    certificate_iurl = models.FilePathField(path="/images")
    is_published = models.BooleanField()

# PROJECT
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_url = models.URLField(max_length = 200, null=True)
    project_git = models.URLField(max_length = 200, null=True)
    project_description = models.TextField(blank=True)
    project_img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    is_opensource = models.BooleanField()

class Contactme(models.Model):
    message = models.TextField()
    subject = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    full_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)