from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'JohnDoe',
        'title': 'Blog Post',
        'content': 'First Post',
        'date_posted': '2020'
    },
    {
        'author': 'JaneDoe',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': '2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 