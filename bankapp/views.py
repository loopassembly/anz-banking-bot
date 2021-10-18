from django.shortcuts import render
from .chatbot import chattxt
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def get_bot_response(request):
     
    userText = request.GET.get('msg')
    chat=chattxt(userText)
    # print(chat.response())
    return HttpResponse(chat.response(), content_type="text/plain")
    