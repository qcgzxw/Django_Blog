from blog.models import Settings


def settings(request):
    site_config = {
        'SITE_TITLE': "test",
        'SITE_SUBTITLE': "test",
        'SITE_DESCRIPTION': "test",
        'SITE_KEYWORDS': "test",
        'SITE_FAVICON': "test",
        'SITE_LOGO': "test",
    }
    if len(Settings.objects.values('title')) is not 0:
        site_config['SITE_TITLE'] = Settings.objects.values('title')[0]['title']
        site_config['SITE_SUBTITLE'] = Settings.objects.values('subtitle')[0]['subtitle']
        site_config['SITE_DESCRIPTION'] = Settings.objects.values('description')[0]['description']
        site_config['SITE_KEYWORDS'] = Settings.objects.values('keywords')[0]['keywords']
        site_config['SITE_FAVICON'] = Settings.objects.values('favicon')[0]['favicon']
        site_config['SITE_LOGO'] = Settings.objects.values('logo')[0]['logo']

    return site_config
