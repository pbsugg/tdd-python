from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    # items = Item.objects.all()
    # return render(request, 'list.html', {'items': items})

    return render(request, 'home.html')
# Create your views here.

def view_list(request):
    # pass
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
