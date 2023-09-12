from django.shortcuts import render, redirect, get_object_or_404
from .models import diary
from django.http import HttpResponse 
from user.models import User
from django.http import Http404


def index(request):
    # diarydata= get_object_or_404(diary,pk=pk) #다이어리 id값에 해당하는 다이어리 상세 객체 받아오기
    return render(request, 'Project/index.html')


def insert_form(request,pk):

    if request.method == 'POST':
        return redirect('mydiary',pk) #홈으로 리다이렉트
    return render(request,'Project/그림일기.html')



def detail_view(request,pk):
    diarydata= get_object_or_404(diary,pk=pk) #다이어리 id값에 해당하는 다이어리 상세 객체 받아오기
    return render(request,'Project/view_detail.html',{'diary':diarydata, 'pk':pk})

def mydiary(request,pk):
    mydiary=diary.objects.filter(account=pk) #accounts id(자신의 id)값 기준으로 다이어리 정렬
    mydiary=mydiary.order_by('diary_id') #필터링 후 정렬
    return render(request, 'Project/index.html', {'mydiary':mydiary})    
    
    
# 저장 함수
def insert(request,pk):   
 
    if request.method == 'POST':
        id=request.session['login_session']
        user=User.objects.get(username=id)
        diaryform= diary() #다이어리 정보 객체 받아오기
        #입력한 값 POST로 받아오기
        diaryform.title = request.POST['title']
        diaryform.date = request.POST['date']
        diaryform.weather = request.POST['weather']
        diaryform.drawing = request.FILES.get('drawing')
        diaryform.content = request.POST['content']
        diaryform.image = request.FILES.get('image')
        diaryform.account=user#user 객체와 외래키 연결(user username값->다이어리 상세정보 글 작성자로 저장(id))
        
        diaryform.save() #객체에 내용 저장
    # return redirect('mydiary',user) #홈으로 리다이렉트

    
 

#GET 요청
def detail2(request):
    id=request.session['login_session']
    user=User.objects.get(username=id)
    pk=user.id
    userdiary=diary.objects.filter(account=pk)
    
    
    if request.method =='GET':
        date=request.GET['date']
        try:
            diarydata=userdiary.get(date=date)
        except diary.DoesNotExist:
            #  return HttpResponse('날짜에 해당하는 글이 없습니다.')
             return redirect('form',pk)
    return render(request,'Project/view_detail.html',{'diary':diarydata})
        
        
    
