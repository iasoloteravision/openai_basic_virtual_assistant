from django.shortcuts import render
from django.http import JsonResponse
from .gpt_handler import generate_response


def home(request):
    return render(request, 'index.html')


def get_response(request):
    user_input = request.GET.get('user_input', '')
    prompt = f"User: {user_input}\nAssistant:"
    assistant_response = generate_response(prompt)
    return JsonResponse({'assistant_response': assistant_response})
