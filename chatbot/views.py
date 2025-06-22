from .services import ask_gpt4
from .models import ChatLog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ChatLog
from .prompts import PROMPTS
from django.http import JsonResponse
from markdown import markdown

@login_required
def chat_view(request):
    phase = request.GET.get('phase') or request.POST.get('phase') or 'emphatize'

    if request.method == 'POST':
        user_input = request.POST.get('message')

        # Ambil histori chat sebelumnya untuk fase yang sama
        logs = ChatLog.objects.filter(user=request.user, phase=phase).order_by('timestamp')
        chat_history = []
        for log in logs:
            chat_history.append({"role": "user", "content": log.user_input})
            chat_history.append({"role": "assistant", "content": log.gpt_response})

        # Kirim ke GPT-4o
        gpt_reply = ask_gpt4(user_input, chat_history=chat_history)

        ChatLog.objects.create(
            user=request.user,
            phase=phase,
            user_input=user_input,
            gpt_response=gpt_reply
        )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'user_input': user_input,
                'gpt_response': markdown(gpt_reply)
            })

        return redirect('chat_view')

    # Untuk GET biasa
    chats = ChatLog.objects.filter(user=request.user, phase=phase).order_by('timestamp')
    prompt_list = PROMPTS.get(phase, [])

    return render(request, 'chatbot/chat.html', {
        'chats': chats,
        'selected_phase': phase,
        'prompt_list': prompt_list
    })