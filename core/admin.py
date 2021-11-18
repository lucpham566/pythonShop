from django.contrib import admin

from core.models import Banner, Service, Subscriber, Video, ShopService, Reviewer

# Register your models here.
admin.site.register(Banner)
admin.site.register(Video)
admin.site.register(Service)
admin.site.register(ShopService)
admin.site.register(Subscriber)
admin.site.register(Reviewer)

