from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.http import HttpResponse

from . models import GetInvolvedPage, VolunteerData, DonationData

from .forms import VolunteerDataForm, DonationDataForm
from django.db.models import Count


def volunteer_application(request):
    # Page = HomePage.objects.all()
    template = "get_involved/get_involved.html"
    Page = GetInvolvedPage.objects.get(slug='get-involved')
    total_volunteers = VolunteerData.objects.values('opportunity_name').annotate(
        total_count=Count('opportunity_name'))
    alert = ''
    if request.method == 'POST':
        if 'form' in request.POST:
            form = VolunteerDataForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                message = form.cleaned_data['message']
                opportunity_name = request.POST.get('opportunity_name')
                approved = False
                form.save()
                alert = 'Your application has been submitted succefully!'
                redirect('/get-involved/')
        elif 'donor_form' in request.POST:
            donor_form = DonationDataForm(request.POST)
            if donor_form.is_valid():
                title = donor_form.cleaned_data['title']
                first_name = donor_form.cleaned_data['first_name']
                middle_name = donor_form.cleaned_data['middle_name']
                last_name = donor_form.cleaned_data['last_name']
                suffix = donor_form.cleaned_data['suffix']
                street = donor_form.cleaned_data['street']
                city = donor_form.cleaned_data['city']
                postal_code = donor_form.cleaned_data['postal_code']
                country = donor_form.cleaned_data['country']
                phone_number = donor_form.cleaned_data['phone_number']
                email = donor_form.cleaned_data['email']
                motive = donor_form.cleaned_data['motive']
                donor_form.save()
                alert = 'Your donation has been received successfully!'
                redirect('/get-involved/')
    else:
        form = VolunteerDataForm()
        donor_form = DonationDataForm()
    # context = {
    #     "body": body,
    # }
    return render(request, template, {'page': Page, 'form': form, 'donor_form': donor_form, 'alert': alert, 'total_volunteers': total_volunteers})
