from django.shortcuts import render

# Create your views here.

def index(request):
    print(">>>>> bbs index")
    return render(request, 'bbs/index.html')

