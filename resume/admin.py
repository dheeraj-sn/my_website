from django.contrib import admin
from .models import Name, Experience, School, College, Skills, Projects, Achievements, Certifications
# Register your models here.
admin.site.register(Name)
admin.site.register(Experience)
admin.site.register(School)
admin.site.register(College)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(Achievements)
admin.site.register(Certifications)