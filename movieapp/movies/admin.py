from django.contrib import admin

from movies.models import Contact, Genre, Movie, Person, Video


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_activate', 'is_home')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('genres', 'language', 'is_activate', 'is_home')
    search_fields = ('title', 'description',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'duty_type')
    search_fields = ('first_name', 'last_name')


admin.site.register(Movie)
admin.site.register(Person, PersonAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
