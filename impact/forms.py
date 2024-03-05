from django import forms

# from datetime import datetime

# currentDateAndTime = datetime.now()


# class CommunityFeedback(forms.Form):
#     date = forms.CharField(currentDateAndTime.strftime("%B %d, %Y"))
#     time = forms.CharField(currentDateAndTime.strftime("%H:%M:%S"))
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)
#     approved = forms.BooleanField(initial=False)

from django import forms

from .models import CommunityFeedback


class CommunityFeedbackForm(forms.ModelForm):
    class Meta:
        model = CommunityFeedback
        exclude = []
