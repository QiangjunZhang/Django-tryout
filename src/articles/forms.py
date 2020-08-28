from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "new-class-name two",
               "rows": 10,
               "cols": 50
               }))
    # pub_date = forms.DateTimeField()

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "fuck" in title:
            raise forms.ValidationError("this is not a validated title")
        else:
            return title


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "new-class-name two",
               "rows": 10,
               "cols": 80
               }))