from django.shortcuts import render , redirect
from DELETE_APP.models import kathir
""" Get """
def getDemo(request):
    display = kathir.objects.all()
    return render(request , 'index.html' , {'key' : display})
""" Insert """ 
def insert(request):
    if request.method == 'POST' :
        Name =request.POST.get('name-value')
        Pass = request.POST.get('pass-value')
        DB = kathir(
            name = Name,
            password = Pass
        )
        DB.save()
        return redirect('home')
    return render(request , 'insert.html')
""" Update """
def update(request , id):
    update_obj = kathir.objects.get(id=id)
    if request.method == 'POST':
        update_obj.name = request.POST.get('name-id')
        update_obj.password = request.POST.get('pass-id')
        update_obj.save()
        return redirect('home')
    return render(request , 'update.html' , {'keys' : update_obj })
""" Delete """
def delete(request , id):
    delete_obj = kathir.objects.get(id=id)
    delete_obj.delete()
    return redirect('home')