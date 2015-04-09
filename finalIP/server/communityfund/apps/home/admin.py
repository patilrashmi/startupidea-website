from django.contrib import admin
from communityfund.apps.home.models import Category, Idea, IdeaRating

class IdeaRatingInline(admin.TabularInline):
    model = IdeaRating
    extra = 1

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'initiator')
    inlines = [
        IdeaRatingInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

