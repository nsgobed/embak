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


class StaffImages(Orderable):

    page = ParentalKey("about_us.AboutUsPage",
                       related_name="staff_details")
    name = models.CharField(max_length=255)
    title = models.CharField(default='Member', max_length=150)
    bios = RichTextField(blank=False)
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
                FieldPanel('name'),
                FieldPanel('title'),
                FieldPanel('image'),
                FieldPanel('bios'),
            ],
            heading='Staff Details'
        ),
    ]

class AboutUsPage(Page):
    template = "about_us/about_us.html"

    max_count = 1

    mission = RichTextField(blank=True)
    history = RichTextField(blank=True)
    our_team = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('mission'),
        FieldPanel('history'),
        FieldPanel('our_team'),
        # MultiFieldPanel(
        #     [
        #         InlinePanel("staff_details", label="Staff member")
        #     ],
        #     heading="Staff Details"
        # ),
        InlinePanel("staff_details", label="Staff Details ")
    ]

    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Pages"
