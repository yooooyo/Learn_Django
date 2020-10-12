from django.contrib import admin

from .models import Question,Choice
# Register your models here.


admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None,  {'fields':['question_text']}),
        ('Date information' ,{'fields':['pub_date']}),
    ]
    

admin.site.register(Question,QuestionAdmin)