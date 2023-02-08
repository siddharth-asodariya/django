"""filter custom tag made for learning"""
import datetime
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import SafeString



register = template.Library()

# @register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(is_safe = True)
@stringfilter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


# The Library.filter() method takes two arguments:
# The name of the filter – a string.
# The compilation function – a Python function (not the name of the function as a string).


# Your filter does not introduce any HTML-unsafe characters (<, >, ', " or &) into the result that were not already present. 
# In this case, you can let Django take care of all the auto-escaping handling for you. 
# All you need to do is set the is_safe flag to True when you register your filter function, like so:
register.filter('cut', cut)
# register.filter('lower', lower)


from django.template.defaultfilters import linebreaksbr, urlize

@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(
        urlize(text, autoescape=autoescape),
        autoescape=autoescape
    )

@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ''


# A few things to note about the simple_tag helper function:

# Checking for the required number of arguments, etc., has already been done by the time our function is called, so we don’t need to do that.
# The quotes around the argument (if any) have already been stripped away, so we receive a plain string.
# If the argument was a template variable, our function is passed the current value of the variable, not the variable itself.

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


# {% show_results poll %}
# <ul>
#   <li>First choice</li>
#   <li>Second choice</li>
#   <li>Third choice</li>
# </ul>

# Here, register is a django.template.Library instance, as before
@register.inclusion_tag('results.html')
def show_results(poll):
    choices = poll.choice_set.all()
    return {'choices': choices}
# <ul>
# {% for choice in choices %}
#     <li> {{ choice }} </li>
# {% endfor %}
# </ul>

# from django.template.loader import get_template
# t = get_template('results.html')
# register.inclusion_tag(t)(show_results)
