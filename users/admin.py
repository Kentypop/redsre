from django.contrib import admin
from .models import Profile, Coupon

class CouponAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

admin.site.register(Profile)
admin.site.register(Coupon, CouponAdmin)