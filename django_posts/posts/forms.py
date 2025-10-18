from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="название", help_text="Введите текст")
    detail = forms.CharField(label="текст поста", widget=forms.Textarea)