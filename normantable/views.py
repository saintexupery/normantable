from django.shortcuts import render


def search_index(request):
    template = 'search/index.html'

    return render(request, template, locals())
