from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdminPanel(admin.ModelAdmin):
	list_display = ('id', 'snippet', 'status', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('text',)

	def snippet(self, obj):
		return str(obj)
	snippet.short_description = 'text'
