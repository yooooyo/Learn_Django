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
    list_filter  = ['pub_date']
    search_fields = ['question_text']
    # Change list pagination
    # search boxes
    # filters
    # date-hierarchies
    # column-header-ordering
    inlines = [ChoiceInline]
    

admin.site.register(Question,QuestionAdmin)

