from django.contrib import admin

from .models import Question,Choice
# Register your models here.


admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None,  {'fields':['question_text']}),
        ('Date information' ,{'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    

admin.site.register(Question,QuestionAdmin)

