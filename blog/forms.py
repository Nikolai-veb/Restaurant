from django import forms

from .models import Comments


class CommentsForm(forms.ModelForm):
        """ Form Comments"""

        class Meta:
            model = Comments
            fields = ("name", "email", "text",)
            widgets = {
                "name": forms.TextInput(attrs={"class": "form-control border"}),
                "email": forms.EmailInput(attrs={"class": "form-control border"}),
                "text": forms.Textarea(attrs={"class": "form-control border"}),

            }