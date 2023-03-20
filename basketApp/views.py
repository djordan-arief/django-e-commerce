from django.shortcuts import render

# Create your views here.
def basket_list(request):
    return render(request, 'basketApp/basket-list.html')