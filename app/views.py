from django.shortcuts import render

def index(request):
    data = request.POST.get('drink')
    print(data)
    return render(request, 'index.html', {'data': data})