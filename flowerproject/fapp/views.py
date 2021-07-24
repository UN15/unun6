from django.shortcuts import render, redirect, get_object_or_404
from .models import Fapp
from django.utils import timezone
from .forms import FappForm

def fmain(request):
    mainobj=Fapp.objects.all()
    return render(request, 'fmain.html', {'mainobj':mainobj})

def fsub(request,id):
    subobj=get_object_or_404(Fapp, pk=id)
    return render(request, 'fsub.html', {'subobj':subobj})

def fnew(request):
    if request.method =='POST':
        fform = FappForm(request.POST, request.FILES)
        if fform.is_valid():
            fcreate = fform.save(commit = False)
            fcreate.pub_date = timezone.now()
            fcreate.save()
            return redirect('fmain')
    else:
        fform = FappForm()
        return render(request, 'fnew.html', {'fform':fform})

def fedit(request, id):
    f_edit= get_object_or_404(Fapp, pk = id)
    if request.method == 'GET':
        f_form = FappForm(instance = f_edit)
        return render(request, 'fedit.html', {'f_edit':f_form})
    else:
        f_form = FappForm(request.POST, request.FILES, instance = f_edit)
        if f_form.is_valid():
            f_edit = f_form.save(commit = False)
            f_edit.pub_date = timezone.now()
            f_edit.save()
        return redirect('fmain')

def fdelete(request, id):
    fdelete = Fapp.objects.get(id = id)
    fdelete.delete()
    return redirect('fmain')

def list(request):
    list = Fapp.objects.all()
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        list = list.filter(title__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'list.html', {'list':list})