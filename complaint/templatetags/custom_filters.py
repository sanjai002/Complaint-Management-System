from django import template
from complaint.models import *
register = template.Library()


@register.simple_tag()
def total1(*args, **kwargs):
    count1 = Complaint.objects.filter(status=None).count()
    return count1

@register.simple_tag()
def total2(*args, **kwargs):
    count2 = Complaint.objects.filter(status="in progress").count()
    return count2

@register.simple_tag()
def total3(*args, **kwargs):
    count3 = Complaint.objects.filter(status="closed").count()
    return count3

register.filter('total1',total1)