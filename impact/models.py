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


# class EducationalInitiatives(Orderable):

#     page = ParentalKey("education.EducationPage",
#                        related_name="educational_initiatives")
#     title = models.CharField(max_length=255)
#     description = RichTextField(blank=False)
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
#                 FieldPanel('title'),
#                 FieldPanel('image'),
#                 FieldPanel('description'),

#             ],
#             heading='+'
#         ),
#     ]


# class EnrolledStudents(Orderable):

#     page = ParentalKey("education.EducationPage",
#                        related_name="enrolled_students")
#     institution = models.CharField(max_length=255)
#     caption = RichTextField(blank=False)
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
#                 FieldPanel('institution'),
#                 FieldPanel('image'),
#                 FieldPanel('caption'),
#             ],
#             heading='+'
#         ),
#     ]


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


class CommunityImpactPage(Page):
    template = "impact/community_impact.html"

    max_count = 1

    testimonials = RichTextField(blank=True)
    statistics_and_achievements = RichTextField(blank=True)
    community_feedback = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('testimonials'),
        # InlinePanel("educational_initiatives",
        #             label="Educational Initiatives"),
        FieldPanel('statistics_and_achievements'),
        # InlinePanel("enrolled_students", label="Enrolled Students"),
        FieldPanel('community_feedback'),
        # InlinePanel("success_stories", label="Success Stories"),
    ]

    class Meta:
        verbose_name = "Community Impact Page"
        verbose_name_plural = "Community Impact Pages"
