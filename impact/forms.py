from django import forms


class CommunityFeedback(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
