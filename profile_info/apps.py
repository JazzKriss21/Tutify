from django.apps import AppConfig


class ProfileInfoConfig(AppConfig):
    name = 'profile_info'

    def ready(self):
        import users.signals #to avoid side affects how import works