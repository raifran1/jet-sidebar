# coding=utf-8
import re
from itertools import chain

from django import template
from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.translation import gettext as _, gettext_lazy

register = template.Library()

# @register.filter()
# def check_permission(user, permissions):
#     """
#     This function run the check permissions the authenticated user for list menu options
#     """
#
#     if user.is_superuser:
#         has_perm = True
#     else:
#         user_groups = []
#
#         if type(permissions) != list:
#             permissions = permissions.split(', ')
#
#         groups_user = user.groups.all()
#         for group in groups_user:
#             user_perms = list(group.permissions.values_list('codename', flat=True).all())
#             for perm in user_perms:
#                 user_groups.append(perm)
#         user_perms = list(user.user_permissions.values_list('codename', flat=True).all())
#
#         user_all_perms = list(sorted(chain(user_perms, user_groups)))
#         if permissions:
#             for perms in permissions:
#                 if str(perms) in user_all_perms:
#                     has_perm = True
#                     break
#                 else:
#                     has_perm = False
#         else:
#             has_perm = False
#
#     return has_perm

@register.simple_tag()
def profile_id(request):
    """
    This function return id profile the user authenticated
    """
    try:
        id = User.objects.get(user=request.user).id
        return id
    except:
        return None


@register.inclusion_tag('admin/_menu_sidebar.html')
def menu_sidbar(user, app):
    """
    New version the admin menu, more scalable and automatized.
    The output of this function generates in the template just a conditional to set the application icon
    """
    try:
        class_icon = apps.get_app_config(app['app_label']).class_icon
    except:
        try:
            class_icon = settings.SID_APP_ICONS[app['app_label']]['class_icon']
        except Exception as e:
            print(_('NotFound icon: '), e)
            print(_('Please read the documentation and implement the necessary settings.'))
            class_icon = None

    if not class_icon:
        class_icon = 'fas fa-exclamation-circle'
    models = ContentType.objects.filter(app_label=app['app_label']).values_list('model', flat=True)
    # permissions = []
    # for model in models:
    #     permission_view = 'view_' + model
    #     permission_add = 'add_' + model
    #     permissions.append(permission_view)
    #     permissions.append(permission_add)
    # app_menu = False
    #
    # if check_permission(user, permissions):
    #     app_menu = app

    for a in app['items']:
        if a['has_perms']:
            app_menu = app
            break
        else:
            app_menu = False

    context = {
        'app_menu': app_menu,
        'class_icon': class_icon,
    }

    return locals()

@register.simple_tag()
def title_apps():
    try:
        _title = settings.SID_TITLE_MENU
    except:
        _title = True

    try:
        _title_text = settings.SID_TEXT_MENU
    except:
        _title_text = ''

    if _title and _title_text:
        return _title_text
    elif _title:
        return _('Applications')
    else:
        return False

@register.simple_tag()
def title_icon_admin():
    '''

    width: icon_small-63px
    width: icon_large-150px
    '''
    text_django = gettext_lazy('Django administration')
    _text = admin.site.site_header
    if _text == text_django:
        _text = 'Django Jet Sidebar'

    try:
        icon_small = settings.SID_ICON_SMALL
    except:
        try:
            icon_small = settings.SID_ICON_LARGE
        except:
            icon_small = False

    try:
        icon_large = settings.SID_ICON_LARGE
    except:
        try:
            icon_large = settings.SID_ICON_SMALL
        except:
            icon_large = False

    if not icon_large and not icon_small:
        text = _text
    else:
        text = False

    try:
        if icon_small['width'] == '':
            icon_small['width'] = '63px'
    except:
        if icon_small:
            icon_small['width'] = '63px'

    try:
        if icon_large['width'] == '':
            icon_large['width'] = '150px'
    except:
        if icon_large:
            icon_large['width'] = '150px'

    context = {
        'text': text,
        'logo_small': icon_small,
        'logo_large': icon_large
    }

    return context

@register.simple_tag()
def url_account():
    try:
        _namespace_url = 'admin:' + re.sub('\.', '_', settings.AUTH_USER_MODEL.lower()) + '_change'
    except:
        _namespace_url = 'admin:auth_user_change'

    return _namespace_url