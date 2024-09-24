from django.contrib import admin

from .views import About, Service, RecentWork,Client

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
