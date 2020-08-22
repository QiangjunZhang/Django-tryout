from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={"class": "new-class-name two",
               "rows": 5,
               "cols": 20
               }))
    price = forms.DecimalField()

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "jon" in title:
            return title
        else:
            raise forms.ValidationError("this is not a validated title")
