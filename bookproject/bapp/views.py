from django.shortcuts import render, redirect, get_object_or_404
from .models import Bapp, Tag
from django.utils import timezone
from .forms import BappForm
import simplejson as json

def bmain(request):
    main=Bapp.objects.all()
    return render(request, 'bmain.html', {'main':main})

def bsub(request,id):
    sub=get_object_or_404(Bapp, pk=id)
    content = sub.body # 본문을 content에 저장
    c_list = content.split(' ') # 공백으로 분리
    t_list = content.split('#') # 공백으로 분리
    return render(request, 'bsub.html', {'sub':sub, 'c_list':c_list, 't_list':t_list})

def bnew(request):
    if request.method =='POST':
        bform = BappForm(request.POST, request.FILES)
        if bform.is_valid():
            bcreate = bform.save(commit = False)
            bcreate.pub_date = timezone.now()
            bcreate.save()

            content = request.POST.get('body') # 본문을 content에 저장
            c_list = content.split(' ') # 공백으로 분리

            for c in c_list:
                if '#' in c: # 만약 #이 붙어있으면 tag 객체를 이용하여 저장한다
                    tag = Tag() 
                    tag.tag_content = c
                    tag.save()
  
                    post_ = Bapp.objects.get(pk=bcreate.pk)
                    
                    post_.tagging.add(tag)

            return redirect('/')
        else:
            return redirect('bnew')
            
    elif request.method =="GET":
        bform = BappForm()
        return render(request, 'bnew.html', {'bform':bform})

def hashtag(request): 
    if request.method == 'POST':
        keyword = request.POST.get('search_button') # keyword를 입력받음
        tag = Tag.objects.filter(tag_content=keyword) # 해당 키워드를 가진 tag 클래스 오픈
        post= Bapp.objects.filter(tagging__in = tag) # 해당 태그를 가진 post 저장
        return render(request, 'search_result.html', {'post':post, 'keyword':keyword})
    elif request.method == 'GET':
        return redirect('/')

def bedit(request, id):
    b_edit= get_object_or_404(Bapp, pk = id)
    if request.method == 'GET':
        b_form = BappForm(instance = b_edit)
        return render(request, 'bedit.html', {'b_edit':b_form})
    else:
        b_form = BappForm(request.POST, request.FILES, instance = b_edit)
        if b_form.is_valid():
            b_edit = b_form.save(commit = False)
            b_edit.pub_date = timezone.now()
            b_edit.save()
        return redirect('bmain')

def bdelete(request, id):
    bdelete = Bapp.objects.get(id = id)
    bdelete.delete()
    return redirect('bmain')

def blist(request):
    list = Bapp.objects.all()
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        list = list.filter(title__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'blist.html', {'list':list})

