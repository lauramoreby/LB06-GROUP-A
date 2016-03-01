from django.contrib import admin
from healthapple.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'readibility_score', 'subjectivity_score', 'sentimentality_score',)

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)