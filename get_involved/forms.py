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

from .models import VolunteerData, DonationData


class VolunteerDataForm(forms.ModelForm):
    class Meta:
        model = VolunteerData
        exclude = ['approved']

    # def as_custom_html(self):
    #     html = ""
    #     for field in self.visible_fields():
    #         html += f"<div>{field.label_tag()}</div>"
    #         html += f"<div>{field}</div>"
    #         if field.errors:
    #             html += f"<div>{field.errors}</div>"
    #     return html


class DonationDataForm(forms.ModelForm):
    class Meta:
        model = DonationData
        exclude = ['']
    def as_custom_html(self):
        html = ""
        for field in self.visible_fields():
            html += f"<div class='row py-2'>"
            html += f"<div class='col-4 text-end'>{field.label_tag()}</div>"
            html += f"<div class='col-8' >{field}</div>"
            html += f"</div>"
            if field.errors:
                html += f"<div>{field.errors}</div>"
        return html
