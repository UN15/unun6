from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Musicapp2
from .forms import Musicapp2Form

def musicmain2(request):
    main2obj = Musicapp2.objects.all()
    return render(request, 'musicmain2.html', {'main2obj': main2obj})

def musicsub2(request, id):
    music2id= get_object_or_404(Musicapp2, pk = id)
    return render(request, 'musicsub2.html', {'music2id': music2id})

def musicnew2(request):
    if request.method =='POST':
        m2_form = Musicapp2Form(request.POST, request.FILES)
        if m2_form.is_valid():
            m2_create = m2_form.save(commit = False)
            m2_create.pub_date = timezone.now()
            m2_create.save()
            return redirect('musicmain2')
    else:
        m2_form = Musicapp2Form()
        return render(request, 'musicnew2.html', {'m2_form':m2_form})

def musicedit2(request, id):
    edit = get_object_or_404(Musicapp2, pk = id)
    if request.method == 'GET':
        edit_form = Musicapp2Form(instance = edit)
        return render(request, 'musicedit2.html', {'m2_edit':edit_form})
    else:
        edit_form = Musicapp2Form(request.POST, request.FILES, instance = edit)
        if edit_form.is_valid():
            edit = edit_form.save(commit = False)
            edit.pub_date = timezone.now()
            edit.save()
        return redirect('musicmain2')


def musicdelete2(request, id):
    m2_delete = Musicapp2.objects.get(id = id)
    m2_delete.delete()
    return redirect('musicmain2')

