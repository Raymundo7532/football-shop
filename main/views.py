from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406404642',
        'name': 'Raymundo Rafaelito Maryos Von Woloblo',
        'class': 'PBP B',
        'app_name' : 'main'
    }

    return render(request, "main.html", context)