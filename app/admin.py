from django.contrib import admin
from .models import category, post, contact, advert, comment, AddVideo

# Register your models here.

admin.site.register(category)
admin.site.register(post)
admin.site.register(contact)
admin.site.register(advert)
admin.site.register(comment)
admin.site.register(AddVideo)



