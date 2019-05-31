from django import template

register = template.Library()


@register.filter
def get_contents(submission, index):
    filename = submission.files[index]

    with open(filename, 'r') as f:
        return f.read()
