from django.contrib import admin

# Register your models here.
from django.contrib import admin

from PkBapp.models import distilerieinfo

from PkBapp.models import distilerie

from PkBapp.models import places

from PkBapp.models import path

from PkBapp.models import review


class distilerieinfoAdmin(admin.ModelAdmin):
    list_display = ('dname', 'washroom', 'parking', 'elevator',
                    'opening_date', 'contact', 'pincode')
    search_fields = ('dname',)
    exclude = ('cost', 'pathid', 'calculated')
    list_filter = ('dname', 'pincode')


class distilerieAdmin(admin.ModelAdmin):
    list_display = ('dname', 'line', 'grade')
    search_fields = ('dname',)
    exclude = ('sid',)
    list_filter = ('dname',)


class placesAdmin(admin.ModelAdmin):
    list_display = ('dname', 'place')
    search_fields = ('dname',)
    exclude = ('sid',)
    list_filter = ('dname',)


class pathAdmin(admin.ModelAdmin):
    list_display = ('fromsid', 'tosid')
    search_fields = ('pathid',)
    list_filter = ('pathid',)


class reviewAdmin(admin.ModelAdmin):
    list_display = ('dname', 'author', 'timest')
    search_fields = ('dname',)
    list_filter = ('dname',)


# Register your models here.

admin.site.register(distilerieinfo, distilerieinfoAdmin)

admin.site.register(distilerie, distilerieAdmin)

admin.site.register(places, placesAdmin)

admin.site.register(path, pathAdmin)

admin.site.register(review, reviewAdmin)