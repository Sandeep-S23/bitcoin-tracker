from django.apps import AppConfig
import os

class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'

    def ready(self):
        from . import job

        if os.environ.get('RUN_MAIN', None) != 'true':
            job.start_scheduler()

