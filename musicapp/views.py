from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Musicapp
from .forms import MusicappForm

def musicmain(request):
    mainobj = Musicapp.objects.all()
    return render(request, 'musicmain.html', {'mainobj': mainobj})

def musicsub(request, id):
    musicid= get_object_or_404(Musicapp, pk = id)
    return render(request, 'musicsub.html', {'musicid': musicid})

def musicnew(request):
    if request.method =='POST':
        m_form = MusicappForm(request.POST)
        if m_form.is_valid():
            m_create = m_form.save(commit = False)
            m_create.pub_date = timezone.now()
            m_create.save()
            return redirect('musicmain')
    else:
        m_form = MusicappForm()
        return render(request, 'musicnew.html', {'m_form':m_form})

def musicedit(request, id):
    edit1 = get_object_or_404(Musicapp, pk = id)
    if request.method == 'GET':
        edit1_form = MusicappForm(instance = edit1)
        return render(request, 'musicedit.html', {'m_edit':edit1_form})
    else:
        edit1_form = MusicappForm(request.POST, request.FILES, instance = edit1)
        if edit1_form.is_valid():
            edit1 = edit1_form.save(commit = False)
            edit1.pub_date = timezone.now()
            edit1.save()
        return redirect('musicmain')

def musicdelete(request, id):
    m_delete = Musicapp.objects.get(id = id)
    m_delete.delete()
    return redirect('musicmain')
