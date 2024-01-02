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


class CurrentInitiativeImage(Orderable):

    page = ParentalKey("home.HomePage",
                       related_name="current_initiatives")

    initiative_title = models.CharField(default='Books Distribution', max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name='+'
    )

    write_up = models.TextField(default='A great project in alieviating the lives of little ones in ....')

    panels = [
        MultiFieldPanel(
             [
                 FieldPanel('initiative_title'),
                 FieldPanel('image'),
                 FieldPanel('write_up'),
                 
             ],
            heading='Initiative image and write up'
        ),
    ]

class CarouselSnippetOrderable(Orderable):
    page = ParentalKey("home.HomePage",
                       related_name="carousel_snippets")

    carousel = models.ForeignKey(
        "home.CarouselSnippet",
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("carousel")
    ]


class CarouselSnippet(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    caption = models.CharField(max_length=255)
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('image'),
                FieldPanel('caption'),
            ],
            heading='Carousel Images and Captions'
        ),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Carousel Snippet"
        verbose_name_plural = "Carousel Snippets"


register_snippet(CarouselSnippet)


class HomePage(Page):
    template = "home/home_page.html"

    max_count = 1
    intro = RichTextField(blank=True)
    overview = RichTextField(blank=True)
    current_initiatives_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('overview'),
        FieldPanel('current_initiatives_text'),
        MultiFieldPanel(
            [
                InlinePanel("carousel_snippets", label="carousel", max_num=10)
            ],
            heading="Carousel(s)"
        ),
        InlinePanel("current_initiatives", label="Current Initiatives ")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


