from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.http import HttpResponse

from . models import CommunityImpactPage, CommunityFeedback

from .forms import CommunityFeedbackForm


def community_impact(request):
    # Page = HomePage.objects.all()
    template = "impact/community_impact.html"
    Page = CommunityImpactPage.objects.get(slug='community-impact')
    feedbacks = CommunityFeedback.objects.all()
    alert = ''
    if request.method == 'POST':
        form = CommunityFeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            approved = False
            form.save()
            alert = 'Feedback has been submitted!'
            redirect('/community-impact/')
    else:
        form = CommunityFeedbackForm()
    # context = {
    #     "body": body,
    # }
    return render(request, template, {'page': Page, 'form': form, 'alert': alert, 'feedbacks': feedbacks})
