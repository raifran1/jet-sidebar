import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'jet_sidebar/templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'jet_sidebar/static')
]

# Topo Menu Sidebar

# Texto
SID_TITLE_MENU = getattr(settings, 'SID_TITLE_MENU', False)
SID_TEXT_MENU = getattr(settings, 'SID_TEXT_MENU', None)

# Icone
SID_ICON_SMALL = getattr(settings, 'SID_ICON_SMALL', None)
SID_ICON_LARGE = getattr(settings, 'SID_ICON_LARGE', None)

# Icons Default In APPS
ICONS_DEFAULT = {
    'auth': {
        'class_icon': 'fas fa-shield-alt',
    },
    'sites': {
        'class_icon': 'fas fa-link',
    }
}

SID_APP_ICONS = getattr(settings, 'SID_APP_ICONS', ICONS_DEFAULT)



