from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.utils.datetime_safe import date
from .models import NoticeText


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')


def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    return render(request, 'index.html', {'name': 'index'})


def profile(request):
    if request.user.is_authenticated:
        notices = NoticeText.objects.all()
        pending_notices = NoticeText.objects.filter(isApproved=False).count()
        posted_notices = NoticeText.objects.filter(isApproved=True).count()
        return render(request, 'hodpage.html',
                      {'notices': notices, 'username': request.user.username, 'pending_notices': pending_notices,
                       'posted_notices': posted_notices})
    else:
        return render(request, 'index.html')


def approve(request):
    notice_id = request.POST['noticeId']
    notice = NoticeText.objects.get(id=notice_id)
    notice.isApproved = True
    notice.save()
    return redirect('profile')


def postnotice(request):
    subject = request.POST['subject']
    content = request.POST['content']
    student = staff = teacher = researcher = for_all = False
    if 'student' in request:
        student = True
    if 'staff' in request:
        staff = True
    if 'teacher' in request:
        teacher = True
    if 'researcher' in request:
        researcher = True
    if 'for_all' in request:
        for_all = True
    print(student)
    print(staff)
    print(teacher)
    print(researcher)
    print(for_all)

    if request.user.is_superuser:
        notice = NoticeText.objects.create(subject=subject, content=content, date=date.today(), isApproved=True,
                                           isStudent=student)
    else:
        notice = NoticeText.objects.create(subject=subject, content=content, date=date.today())
    notice.save()
    print('notice saved')
    return redirect('profile')
