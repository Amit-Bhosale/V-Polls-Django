from django.contrib import admin
from .models import Contact,Votes,Member,Notice
from django.contrib.sessions.backends.db import SessionStore
# Register your models here.
admin.site.register(Contact)
admin.site.register(Votes)
admin.site.register(Member)
admin.site.register(Notice)
