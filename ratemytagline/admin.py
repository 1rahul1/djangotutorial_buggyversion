from django.contrib import admin
from .models import tagLine

#I am not able to see tagLine in the administrator console. Can you make it visible in the admin console?

from django.contrib import admin
from .models import Post
admin.site.register(Post)
