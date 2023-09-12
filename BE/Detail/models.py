from django.db import models
from user.models import User

class diary(models.Model):
    diary_id=models.AutoField(primary_key=True) #diary id 값
    title=models.CharField(max_length=50, null=True,blank=True)   #제목
    date=models.DateField(auto_now=False, null=True,blank=True)   #날짜
    weather=models.CharField(max_length=10,blank=True, null=True)  #프론트에서 우산, 구름, 맑음 선택해서 보내면 DB 저장
    image = models.ImageField(max_length=255,upload_to='images/', blank=True, null=True)    #사진 업로드
    drawing=models.ImageField(upload_to='drawing/', blank=True, null=True)   #그림 업로드
    content=models.TextField(blank=True, null=True)  #내용
    
    account=models.ForeignKey(User, null=True, on_delete=models.CASCADE)#회원 삭제되면 다이어리도 함께 삭제됨.
    
    
    
    def __str__(self):
        return self.title
    

