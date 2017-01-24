from django.contrib import admin
from .models import games, mouse

# Register your models here.
class gamesAdmin(admin.ModelAdmin):
	class Meta:
		model = games

admin.site.register(games, gamesAdmin)

class mouseAdmin(admin.ModelAdmin):
	class Meta:
		model = mouse

admin.site.register(mouse, mouseAdmin)