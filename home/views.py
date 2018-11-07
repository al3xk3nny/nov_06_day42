from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Topic
from .forms import TopicForm, BookForm

# Create your views here.

def say_hello(request):
    this_topics = Topic.objects.all()
    
    if "id" in request.GET:
        topic_id = request.GET["id"]
        this_books = Book.objects.filter(topic=topic_id)
    else:
        this_books = Book.objects.all()
    
    return render(request, "home/index.html", {"books": this_books, "topics": this_topics})
    

def add_topic(request):
    form = TopicForm()
    return render(request, "home/add_topic.html", {"form": form})
    

def add_topic_for_real(request):
    
    form = TopicForm(request.POST)
    form.save()
    
    return redirect("/")


def add_book(request):
    form = BookForm()
    return render(request, "home/add_book.html", {"form": form})


def add_book_for_real(request):
    
    form = BookForm(request.POST)
    form.save()
    
    return redirect("/")