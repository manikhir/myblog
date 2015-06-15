from django import forms
from pagedown.widgets import PagedownWidget
from django.contrib.admin import widgets
from blogs.models import  AddCategory,Blog
from django.contrib.comments.models import Comment
from django.forms.widgets import HiddenInput
from datetimewidget.widgets import DateTimeWidget
from multiupload.fields import MultiFileField
from django.forms.formsets import formset_factory

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategory
        fields = ['title','slug']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        # files = MultiFileField(max_num = 10, min_num = 1)
        title = forms.CharField(required = True)
        description = forms.CharField(required = True)
        widgets = {
            'description' : PagedownWidget(),
            'date': DateTimeWidget(attrs={'id':"datepicker"}, usel10n = True)
        }
        fields = ['title','description','date' ,'category','tag']

    def form_valid(self, form):
            for each in form.cleaned_data['blog']:
                Blog.objects.create(file=each)
            return super(ArticleForm, self).form_valid(form)




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'content_type' : HiddenInput(),
            'object_pk': HiddenInput(),
        }

        fields=['user_name','user_email','comment','content_type','object_pk',]


class ImageForm(forms.ModelForm):
    class Meta:
        fields=['image']