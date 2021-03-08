from django.shortcuts import render


def index(request):
    context = {
        'title':'Maldev',
        'subjudul':'Selamat datang di Maldev',
    }

    return render(request,'index.html',context)