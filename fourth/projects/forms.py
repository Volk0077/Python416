from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):

    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class':'input'})

        # Поля становятся как в шаблоне (вытянутые на всю страницу), но легче сделать как вверху

        # self.fields['title'].widget.attrs.update({'class':'input'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

    class Meta:
        model = Project
        fields = ['title', 'featured_images','description', 'demo_link', 'source_link', 'tags']
        widgets = {'tags': forms.CheckboxSelectMultiple()}

    


