from django.shortcuts import render, redirect, get_object_or_404
from .models import Hobby, Message
from django.utils import timezone
from .forms import HobbyForm, MessageForm
from django.http import HttpResponse
from django.core.mail import send_mail

def hmain(request):
    h_main=Hobby.objects.all()
    return render(request, 'hmain.html', {'h_main':h_main})

def hsub(request,id):
    h_sub=get_object_or_404(Hobby, pk=id)
    return render(request, 'hsub.html', {'h_sub':h_sub})

def hnew(request):
    if request.method =='POST':
        hform = HobbyForm(request.POST, request.FILES)
        if hform.is_valid():
            hcreate = hform.save(commit = False)
            hcreate.pub_date = timezone.now()
            hcreate.save()
            return redirect('hmain')
    else:
        hform = HobbyForm()
        return render(request, 'hnew.html', {'hform':hform})

def hedit(request, id):
    h_edit= get_object_or_404(Hobby, pk = id)
    if request.method == 'GET':
        h_form = HobbyForm(instance = h_edit)
        return render(request, 'hedit.html', {'h_edit':h_form})
    else:
        h_form = HobbyForm(request.POST, request.FILES, instance = h_edit)
        if h_form.is_valid():
            h_edit = h_form.save(commit = False)
            h_edit.pub_date = timezone.now()
            h_edit.save()
        return redirect('hmain')

def hdelete(request, id):
    hdelete = Hobby.objects.get(id = id)
    hdelete.delete()
    return redirect('hmain')

def email(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
                'name':name,
                'email':email,
                'subject':subject,
                'message':message
        }

        message = '''
        New message:{}

        From:{}   
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['jaeun101501@gmail.com'])
        return HttpResponse('메일이 전송되었습니다.')
    return render(request, 'email.html', {})

def mmain(request):
    m_main=Message.objects.all()
    return render(request, 'mmain.html', {'m_main':m_main})

def msend(request):
    m_send=Message.objects.all()
    return render(request, 'msend.html', {'m_send':m_send})

def msub(request, id):
    m_sub=get_object_or_404(Message, pk=id)
    return render(request, 'msub.html', {'m_sub':m_sub})

def mnew(request):
    if request.method =='POST':
        mform = MessageForm(request.POST, request.FILES)
        if mform.is_valid():
            mcreate = mform.save(commit = False)
            mcreate.save()
            return redirect('mmain')
    else:
        mform = MessageForm()
        return render(request, 'mnew.html', {'mform':mform})
