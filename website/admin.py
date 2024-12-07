from django.contrib import admin
from website import models

# Register your models here.
# from .models import Feature, About, Counter, Service, Challenge, Project, WhyChooseUs, Testimonial, Blog, Partner, Slider
# class ProductAdmin(admin.ModelAdmin):
# admin.site.register(models.Product,ProductAdmin)

admin.site.register(models.Feature)
admin.site.register(models.About)
admin.site.register(models.Counter)
admin.site.register(models.Service)
admin.site.register(models.Challenge)
admin.site.register(models.Project)
admin.site.register(models.WhyChooseUs)
admin.site.register(models.Testimonial)
admin.site.register(models.Blog)
admin.site.register(models.Partner)
admin.site.register(models.Slider)

admin.site.register(models.Header)
# admin.site.register(models.Midel)
admin.site.register(models.Security)
admin.site.register(models.Cardsection)

admin.site.register(models.Servicesection)
admin.site.register(models.RecentSection)
admin.site.register(models.Featuredpost)
admin.site.register(models.Catepost)

admin.site.register(models.Contcard)