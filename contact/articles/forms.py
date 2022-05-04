from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        # fields=['article','name','image','email','website','message']
        fields='__all__'
        exclude=['article']

    def __init__(self,*args,**kwargs):
        super(CreateCommentForm,self).__init__(*args,**kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']=field_name

