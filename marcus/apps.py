from django.apps import AppConfig, apps
from django.db import models

import secretballot


class MarcusAppConfig(AppConfig):
    name = 'marcus'
    verbose_name = 'marcus'

    def ready(self):
        article_model = apps.get_model("marcus", "Article")
        secretballot.enable_voting_on(article_model)
