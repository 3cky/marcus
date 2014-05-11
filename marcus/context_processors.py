from django.contrib.sites.models import Site
from django.conf import settings


def marcus_context(request):
    return {
        'site': Site.objects.get_current(),
        'MARCUS_TITLE': settings.MARCUS_TITLE,
        'MARCUS_SUBTITLE': settings.MARCUS_SUBTITLE,
        'MARCUS_GA_ACCOUNT_ID' : settings.MARCUS_GA_ACCOUNT_ID,
        'MARCUS_GA_ACCOUNT_NAME' : settings.MARCUS_GA_ACCOUNT_NAME,
    }
