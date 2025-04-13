from .services import ask_gpt4
from .models import ChatLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatLog

@login_required
def chat_view(request):
    phase = request.GET.get('phase') or request.POST.get('phase') or 'emphatize'

    if request.method == 'POST':
        user_input = request.POST.get('message')
        gpt_reply = ask_gpt4(user_input)

        ChatLog.objects.create(
            user=request.user,
            phase=phase,
            user_input=user_input,
            gpt_response=gpt_reply
        )

    chats = ChatLog.objects.filter(user=request.user, phase=phase).order_by('timestamp')

    return render(request, 'chatbot/chat.html', {
        'chats': chats,
        'selected_phase': phase
    })

