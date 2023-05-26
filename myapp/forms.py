from django import forms
from .models import Product

class ProductForms(forms.ModelForm):
    title = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 120,
                            }
                            )
                        )
    summary = forms.CharField(required=False)
    price = forms.DecimalField(initial=708.00)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'summary',
            'price',
        ]
    def clean_title(self, *args, ** kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
            return title
        

    def clean_email(self, *args, ** kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
            return email
        
            

class RawProductForm(forms.Form):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 120,
                            }
                            )
                        )
    summary = forms.CharField(required=False)
    price = forms.DecimalField(initial=708.00)
    