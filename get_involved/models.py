from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
)

from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey


class VolunteerData(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()
    opportunity_name = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VolunteerOpportunities(Orderable):

    page = ParentalKey("get_involved.GetInvolvedPage",
                       related_name="volunteer_opportunities")
    title = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('image'),
            ],
            heading='+'
        ),
    ]


class DonationData(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    motive = models.TextField()

    def __str__(self):
        return self.name



class DonationTypes(Orderable):

    page = ParentalKey("get_involved.GetInvolvedPage",
                       related_name="donation_types")
    type = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('type'),
                FieldPanel('image'),
            ],
            heading='+'
        ),
    ]


# class SuccessStories(Orderable):

#     page = ParentalKey("education.EducationPage",
#                        related_name="success_stories")
#     name = models.CharField(max_length=255)
#     course_pursued = RichTextField(blank=True, max_length=255)
#     current_endevours = RichTextField(blank=True)
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )

#     panels = [
#         MultiFieldPanel(
#             [
#                 FieldPanel('name'),
#                 FieldPanel('image'),
#                 FieldPanel('course_pursued'),
#                 FieldPanel('current_endevours'),
#             ],
#             heading='+'
#         ),
#     ]


class GetInvolvedPage(Page):
    template = "get_involved/get_involved.html"

    max_count = 1

    volunteer_opportunities_intro = RichTextField(blank=True)
    donate= RichTextField(blank=True)
    join_our_programs = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('volunteer_opportunities_intro'),
        InlinePanel("volunteer_opportunities",
                    label="Volunteer Opportunities"),
        FieldPanel('donate'),
        InlinePanel("donation_types", label="Donation Types"),
        FieldPanel('join_our_programs'),
        # InlinePanel("success_stories", label="Success Stories"),
    ]

    class Meta:
        verbose_name = "Get Involved Page"
        verbose_name_plural = "Get Involved Pages"
