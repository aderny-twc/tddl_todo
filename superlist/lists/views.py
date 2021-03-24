from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    """Home page"""
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'lists/home.html')
    return render(request, 'lists/home.html', {
            'new_item_text': request.POST.get('item_text', ''),
        })
