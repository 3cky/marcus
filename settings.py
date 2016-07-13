import os
import imp

PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
STORAGE_ROOT = os.path.join('/storage', PROJECT_NAME)
LOCALE_PATHS = (
    os.path.join(imp.find_module('marcus')[1], 'locale'),
)

MARCUS_PAGINATE_BY = 20
MARCUS_ARTICLES_ON_INDEX = 10
MARCUS_COMMENTS_ON_INDEX = 10
MARCUS_COMMENT_EXCERPTS_ON_INDEX = 2
MARCUS_ITEMS_IN_FEED = 20
MARCUS_AUTHOR_ID = 1
MARCUS_TAG_MINIMUM_ARTICLES = 0

# Specify blog names:
from django.utils.translation import ugettext_lazy as _
MARCUS_TITLE = _('Blog')
MARCUS_SUBTITLE = _('Sample blog')

MARCUS_DESCRIPTION = _('')
MARCUS_KEYWORDS = _('')

MARCUS_PROFILE_IMAGE = ''

# You can specify #hashtag or @name as suffix for Twitter:
MARCUS_SHARE_SUFFIX = "#marcus"

# Facebook App ID for "Share" button
MARCUS_SHARE_FB_APP_ID = ''

# Specify a fields which will used in search:
MARCUS_SEARCH_FIELDS = [
    'slug', 'title_ru', 'title_en', 'text_ru', 'text_en',
    'categories__slug', 'categories__title_ru', 'categories__title_en',
]

# Google Analytics tracking code variables
MARCUS_GA_ACCOUNT_ID = ''
MARCUS_GA_ACCOUNT_NAME = ''

# OpenID sessions dir. OpenID authentication will not work without it.
SCIPIO_STORE_ROOT = os.path.join(STORAGE_ROOT, 'scipio')

# URL passed to OpenID-provider to identify site that requests authentication.
# Should not end with '/'.
# Complete site URL is passed if the value is empty.
SCIPIO_TRUST_URL = ''

# Akismet is a spam filtering service.
# Without the key will not work comments.
# You can receive the key here https://akismet.com/signup/
SCIPIO_AKISMET_KEY = ''

SCIPIO_USE_CONTRIB_SITES = True

AUTHENTICATION_BACKENDS = (
    'scipio.authentication.OpenIdBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.github.GithubOAuth2',
    'social.backends.vk.VKOAuth2',
    # Add other social auth backends here if needed
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'marcus.context_processors.marcus_context',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

MEDIA_ROOT = os.path.join(STORAGE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(STORAGE_ROOT, 'static')
STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'marcus',
    'scipio',
    'social.apps.django_app.default',
)

MARCUS_WORDPRESS_IMPORTER = {
    'ARTICLE_PIPELINES': (
        'marcus.wordpress_importer.pipelines.CodecolorerToHighlightJsPipeline',
        'marcus.wordpress_importer.pipelines.WpContentUploadsToMediaPipeline',
        'marcus.wordpress_importer.pipelines.BbCodeDetector',
        'marcus.wordpress_importer.pipelines.EscapeTheUnderscore',
        # 'marcus.wordpress_importer.pipelines.ChangeUrlToArticleForImagePipeline',
        # 'marcus.wordpress_importer.pipelines.RemoveImgClassPipeline',
        # 'marcus.wordpress_importer.pipelines.HtmlToMarkdownPipeline',
    ),
    # 'CATEGORY_PIPELINES': tuple(),
    # 'TAG_PIPELINES': tuple(),
    'COMMENT_PIPELINES': (
        'marcus.wordpress_importer.pipelines.CodecolorerToHighlightJsPipeline',
    ),
    'ALLOW_DOMAINS': (
        'my-old-blog-on-wordpress.org',
        'www.my-old-blog-on-wordpress.org',
    ),
}

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
#    'social.pipeline.mail.mail_validation',
#    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'marcus.social.pipeline.save_profile',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_PROVIDERS = None
# Example:
# SOCIAL_AUTH_PROVIDERS = collections.OrderedDict([
#                             ('facebook', 'Facebook'),
#                             ('twitter', 'Twitter'),
#                             ('google-oauth2', 'Google'),
#                             ('github', 'GitHub'),
#                             ('vk-oauth2', 'VK.com'),
#                         ])

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_KEY = ""
SOCIAL_AUTH_FACEBOOK_SECRET = ""

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_OAUTH2_KEY = ''
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''
