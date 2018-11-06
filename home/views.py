from django.shortcuts import render, HttpResponse
from .models import Book, Topic

# Create your views here.

def say_hello(request):
    this_topics = Topic.objects.all()
    
    if "id" in request.GET:
        topic_id = request.GET["id"]
        this_books = Book.objects.filter(topic=topic_id)
    else:
        this_books = Book.objects.all()
    
    return render(request, "home/index.html", {"books": this_books, "topics": this_topics})    