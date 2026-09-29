from django.shortcuts import render, redirect

PROJECTS = [
    {
        "title": "To-Do List",
        "desc": "A task management app built with Python.",
        "image": "project1.jpg",
        "video": "project1.mp4",
        "github": "#",
    },
    {
        "title": "Student Grade Management System",
        "desc": "A Python system to record and manage student grades.",
        "image": "project2.jpg",
        "video": "project2.mp4",
        "github": "#",
    },
    {
        "title": "Gym Fitness Website",
        "desc": "A fitness website built with HTML, CSS and JavaScript.",
        "image": "project3.jpg",
        "video": "project3.mp4",
        "github": "#",
    },
    {
        "title": "Expense Tracker",
        "desc": "A Python app to track daily expenses and budgets.",
        "image": "project4.jpg",
        "video": "project4.mp4",
        "github": "#",
    },
    {
        "title": "Random Quotes",
        "desc": "An HTML, CSS and JavaScript random quotes generator.",
        "image": "project5.jpg",
        "video": "project5.mp4",
        "github": "#",
    },
]

def home(request):
    success = request.GET.get('sent') == '1'
    return render(request, 'index.html', {'success': success})

def projects(request):
    return render(request, 'projects.html', {'projects': PROJECTS})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"New message from {name} ({email}): {message}")
        return redirect('/?sent=1#contact')