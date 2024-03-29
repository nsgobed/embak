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


class ProgramsAndActivities(Orderable):

    page = ParentalKey("empowerment.EmpowermentPage",
                       related_name="programs_and_activities")
    title = models.CharField(max_length=255)
    description = RichTextField(blank=False)
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
                FieldPanel('description'),

            ],
            heading='+'
        ),
    ]


class CommunitySuccessStories(Orderable):

    page = ParentalKey("empowerment.EmpowermentPage",
                       related_name="community_success_stories")
    title = models.CharField(max_length=255)
    description = RichTextField(blank=False)
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
                FieldPanel('description'),
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


class EmpowermentPage(Page):
    template = "empowerment/empowerment.html"

    max_count = 1

    programs_and_activities_intro = RichTextField(blank=True)
    community_success_stories_intro = RichTextField(blank=True)
    get_involved = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('programs_and_activities_intro'),
        InlinePanel("programs_and_activities",
                    label="Programs Activities"),
        FieldPanel('community_success_stories_intro'),
        InlinePanel("community_success_stories",
                    label="Community Success Stories"),
        FieldPanel('get_involved'),
        # InlinePanel("success_stories", label="Success Stories"),
    ]

    class Meta:
        verbose_name = "Empowerment Page"
        verbose_name_plural = "Empowerment Pages"
