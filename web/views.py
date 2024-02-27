from django.shortcuts import render

def index(request):
    name = "John"  # Replace "John" with the actual name you want to pass to the template
    context = {
        'name': name,
    }
    return render(request, 'index.html', context)
