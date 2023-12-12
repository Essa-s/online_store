from django.shortcuts import render
from .models import Men, Category
# Create your views here.
def men(request):
    items = Men.objects.all()
    category = Category.objects.all()
 
    context = {
        'items': items,
        'catgory': category,
       
    }

    return render(request, 'men.html', context = context)

