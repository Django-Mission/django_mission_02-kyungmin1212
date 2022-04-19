# Generated by Django 4.0.4 on 2022-04-19 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=126, verbose_name='질문')),
                ('category', models.CharField(choices=[('G', '일반'), ('A', '계정'), ('E', '기타')], max_length=2, verbose_name='카테고리')),
                ('answer', models.TextField(verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updater', models.CharField(max_length=16, verbose_name='최종 수정자')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
