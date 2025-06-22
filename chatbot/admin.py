from django.contrib import admin
from .models import ChatLog

@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'phase', 'user_input_short', 'gpt_response_short', 'timestamp')
    list_filter = ('phase', 'user')
    search_fields = ('user__username', 'user_input', 'gpt_response')

    def user_input_short(self, obj):
        return obj.user_input[:50] + "..." if len(obj.user_input) > 50 else obj.user_input
    user_input_short.short_description = "User Input"

    def gpt_response_short(self, obj):
        return obj.gpt_response[:50] + "..." if len(obj.gpt_response) > 50 else obj.gpt_response
    gpt_response_short.short_description = "GPT Response"
