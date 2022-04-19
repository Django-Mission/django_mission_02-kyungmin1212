from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    question = models.CharField(verbose_name='질문',max_length=126)
    category_choice= [
        ('G','일반'),
        ('A','계정'),
        ('E','기타')
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=category_choice
    )
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE ,null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시',auto_now_add=True)
    updater = models.CharField(verbose_name='최종 수정자',max_length=16)
    update_at = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True) 
