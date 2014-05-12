from django.contrib.sites.models import Site
from django.conf import settings
from django.utils import translation

def marcus_context(request):
    language = 'en' if request.path.endswith('/en/') else None
    if language:
        translation.activate(language)
    return {
        'site': Site.objects.get_current(),
        'language': language,
        'MARCUS_TITLE': settings.MARCUS_TITLE,
        'MARCUS_SUBTITLE': settings.MARCUS_SUBTITLE,
        'MARCUS_GA_ACCOUNT_ID' : settings.MARCUS_GA_ACCOUNT_ID,
        'MARCUS_GA_ACCOUNT_NAME' : settings.MARCUS_GA_ACCOUNT_NAME,
    }
