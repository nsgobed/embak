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


class CommunityFeedback(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StatisticsAndAchievements(Orderable):

    page = ParentalKey("impact.CommunityImpactPage",
                       related_name="statistics_and_achievements")
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


class Testimonials(Orderable):

    page = ParentalKey("impact.CommunityImpactPage",
                       related_name="testimonials")
    author_name = models.CharField(max_length=255)
    testimonial = RichTextField(blank=False)
    # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('author_name'),
                # FieldPanel('image'),
                FieldPanel('testimonial'),
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


class CommunityImpactPage(Page):
    template = "impact/community_impact.html"

    max_count = 1

    testimonials_intro = RichTextField(blank=True)
    statistics_and_achievements_intro = RichTextField(blank=True)
    community_feedback = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        # InlinePanel("statistics_and_achievements",
        #             label="Statistics and Achievements"),
        FieldPanel('statistics_and_achievements_intro'),
        InlinePanel("statistics_and_achievements",
                    label="Statistics and Achievements"),
        FieldPanel('testimonials_intro'),
        InlinePanel("testimonials", label="Testimonials"),
        FieldPanel('community_feedback'),
    ]

    class Meta:
        verbose_name = "Community Impact Page"
        verbose_name_plural = "Community Impact Pages"
