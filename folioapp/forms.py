from django import forms


class CommentForm(forms.Form):
    """Form for the Comment model"""
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form_input",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form_input",
            "placeholder": "Leave a comment!"
        })
    )

class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            "class": "form_input",
            "placeholder": "Insert your name"
        })
    )
    email = forms.EmailField(
        max_length=120,
        widget=forms.TextInput(attrs={
            "class": "form_input",
            "placeholder": "Insert your email"
        })
    )
    subject = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            "class": "form_input",
            "placeholder": "Insert your subject"
        })
    )
    message = forms.CharField(
        max_length=120,
        widget=forms.Textarea(attrs={
            "class": "form_input",
            "placeholder": "Write you message"
        })
    )