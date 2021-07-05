from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Cookierun
from .forms import CookierunForm

def gamemain(request):
    gmain = Cookierun.objects
    g_list = Cookierun.objects.all()
    paginator = Paginator(g_list, 2)
    g_page = request.GET.get('g_page')
    g_posts = paginator.get_page(g_page)
    return render(request, 'gamemain.html', {'gmain': gmain, 'g_posts': g_posts})

def gamesub(request, id):
    gsub = get_object_or_404(Cookierun, pk = id)
    return render(request, 'gamesub.html', {'gsub': gsub})

def gamenew(request):
    if request.method =='POST':
        new_form = CookierunForm(request.POST, request.FILES)
        if new_form.is_valid():
            new_create = new_form.save(commit = False)
            new_create.pub_date = timezone.now()
            new_create.save()
            return redirect('gamemain')
    else:
        new_form = CookierunForm()
        return render(request, 'gamenew.html', {'new_form':new_form})

def gameedit(request, id):
    gedit= get_object_or_404(Cookierun, pk = id)
    if request.method == 'GET':
        g_form = CookierunForm(instance = gedit)
        return render(request, 'gameedit.html', {'g_edit':g_form})
    else:
        g_form = CookierunForm(request.POST, request.FILES, instance = gedit)
        if g_form.is_valid():
            gedit = g_form.save(commit = False)
            gedit.pub_date = timezone.now()
            gedit.save()
        return redirect('gamemain')

def gamedelete(request, id):
    gdelete = Cookierun.objects.get(id = id)
    gdelete.delete()
    return redirect('gamemain')
