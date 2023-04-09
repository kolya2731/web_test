from django.shortcuts import render

def index(request):
    data = {
        'title': 'ГОЛОВНА',
        'values': ['hello', 'hi', '11112124'],
        'obj': {
            'car': 'lanos',
            'age': '17',
            'hobby': 'play chess'
        }

    }

    return render(request,'main/index.html',data)
def index_2(request):
    return render(request,'main/about.html')