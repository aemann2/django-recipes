from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Recipe, RecipeIngredient, User

# Register your models here.

# a more sophisticated way to handle our data, using StackedInline and custom admin field ordering
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ["name", "quantity", "unit"]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(User, UserAdmin)