from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "new-class-name two",
               "rows": 5,
               "cols": 20
               }))
    pub_date = forms.DateTimeField()

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "jon" in title:
            return title
        else:
            raise forms.ValidationError("this is not a validated title")
