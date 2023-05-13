from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def cut_url_to_front(value):
    url = "{}/api/".format(getattr(settings, 'LANGUAGE_CODE'))
    return value.replace(url, '')


def parse_paragraph(text):
    return f'<p>{text}</p>'


def parse_image(url, caption):
    return f'<img style="max-height: 400px; max-width: 100%;" src="{url}" /><br/><p>{caption}</p>'


def parse_list(items):
    list_li = ''.join([f'<li>{item}</li>' for item in items])
    return f'<ul>{list_li}</ul>'


def parse_header(text, level):
    return f'<h{level}>{text}</h{level}>'


@register.filter(is_safe=True)
def editorjs(value):
    if not isinstance(value, dict):
        return value

    html_list = []
    for item in value['blocks']:
        if item['type'] == 'paragraph':
            html_list.append(parse_paragraph(
                item['data']['text'].replace('&nbsp;', ' ')))
        elif item['type'] == 'Header':
            html_list.append(parse_header(
                item['data']['text'].replace('&nbsp;', ' '), item['data']['level']))
        elif item['type'] == 'List':
            html_list.append(parse_list(item['data']['items']))
        elif item['type'] == 'Image':
            html_list.append(parse_image(item['data']['file']['url'], item['data']['caption'].replace('&nbsp;', ' ')))

    return mark_safe(''.join(html_list))
