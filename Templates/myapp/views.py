from django.shortcuts import render

from django.shortcuts import render

def index(request):
    context = {
        'title': 'Templates',
        'items': ['Elemento 1', 'Elemento 2', 'Elemento 3']
    }
    return render(request, 'mi_template.html', context)