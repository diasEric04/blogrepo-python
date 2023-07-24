from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home'
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )
