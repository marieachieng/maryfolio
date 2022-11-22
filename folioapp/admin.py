from django.contrib import admin
from .models import User, Post, Job, Project, Certification, Skill, Education, Contactme, Socialaccount, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Contactme)
admin.site.register(Socialaccount)
admin.site.register(Category)