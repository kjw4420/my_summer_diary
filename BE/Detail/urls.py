from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/form/insert/',views.insert, name='insert'), #실제 저장 함수(자바스크립트 땜에 분리함)   
    path('<int:pk>/form/',views.insert_form, name='form'),  #작성폼  diary/form/
    path('detail/<int:pk>',views.detail_view, name='detail_view'),  #다이어리 상세페이지 diary/detail/<diary_id>
    path('<int:pk>',views.mydiary,name='mydiary'),
    path('',views.index,name='index'), #달력나오는 화면 diary////이거 고침~~
    path('detail2',views.detail2, name='detail2'),  #수정수정수정
]
