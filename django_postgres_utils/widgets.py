# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import django
from django import forms
from django.conf import settings
from django.contrib.admin.templatetags.admin_static import static
from django.contrib.admin.widgets import AdminTextareaWidget
from django.template.loader import get_template
from django.utils.safestring import mark_safe

__all__ = [
    'AdminHStoreWidget'
]


class BaseAdminHStoreWidget(AdminTextareaWidget):
    """
    Base admin widget class for default-admin and grappelli-admin widgets
    """
    admin_style = 'default'

    @property
    def media(self):
        internal_js = [
            "underscore-min.js",
            "hstore-widget.js"
        ]

        js = [static("admin/js/django_postgres_utils/%s" % path) for path in internal_js]

        return forms.Media(js=js)

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        # it's called "original" because it will be replaced by a copy
        attrs['class'] = 'hstore-original-textarea'

        # get default HTML from AdminTextareaWidget
        html = super(BaseAdminHStoreWidget, self).render(name, value, attrs)

        # prepare template context
        template_context = {
            'field_name': name,
            'STATIC_URL': settings.STATIC_URL,
            'use_svg': django.VERSION >= (1, 9),  # use svg icons if django >= 1.9
        }
        # get template object
        template = get_template('django_postgres_utils/hstore_%s_widget.html' % self.admin_style)
        # render additional html
        if django.VERSION < (1, 11):
            from django.template import Context
            template_context = Context(template_context)
        additional_html = template.render(template_context)

        # append additional HTML and mark as safe
        html = html + additional_html
        html = mark_safe(html)

        return html


class DefaultAdminHStoreWidget(BaseAdminHStoreWidget):
    """
    Widget that displays the HStore contents
    in the default django-admin with a nice interactive UI
    """
    admin_style = 'default'


class GrappelliAdminHStoreWidget(BaseAdminHStoreWidget):
    """
    Widget that displays the HStore contents
    in the django-admin with a nice interactive UI
    designed for django-grappelli
    """
    admin_style = 'grappelli'


if 'grappelli' in settings.INSTALLED_APPS:
    AdminHStoreWidget = GrappelliAdminHStoreWidget
else:
    AdminHStoreWidget = DefaultAdminHStoreWidget
