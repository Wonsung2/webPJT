
from django.shortcuts import HttpResponse, render

def index(request) :
    # 업무로직 처리
    print('>>>>>>>> aiWEB index')
    return render(request , 'index.html')