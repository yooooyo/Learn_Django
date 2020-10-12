from django.contrib import admin

from .models import Question,Choice
# Register your models here.


admin.site.register(Choice)

##############################################
# use
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
# or
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
#############################################

class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None,  {'fields':['question_text']}),
        ('Date information' ,{'fields':['pub_date']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    

admin.site.register(Question,QuestionAdmin)

