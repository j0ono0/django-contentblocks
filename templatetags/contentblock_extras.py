from markdown import markdown as md
from django import template
from django.db.models import Q
from ..models import ContentBlock
from django.utils.safestring import mark_safe
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('contentblocks/contentblock.html')
def contentblock(location, user=None):

    # TODO: review authentication (add group example?)
    
    if not user:
        groups = ['all']
    elif user.is_authenticated:
        groups = ['all','authenticated']
    else:
        groups = ['all','anonymous']

    
    in_group = Q(display_group__in=groups)
    at_location = Q(location = location)
    after_start = Q(start_datetime__lt = timezone.now())
    before_end = Q(end_datetime__gt = timezone.now())
    no_end = Q( end_datetime__isnull = True)
    blocks = ContentBlock.objects.filter(in_group, at_location & after_start & (before_end | no_end))
    # If user is authenticated parse content to personalise.
    for block in blocks:
        if user and user.is_authenticated:
            db_template = template.Template(block.content) # get from db
            block.content = db_template.render(template.Context({'user':user}))

    return {
        'content': blocks
        }


def markdown(value):
    """Converts markdown to html"""
    return md(value)

register.filter('markdown', markdown)