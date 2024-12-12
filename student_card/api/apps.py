from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

# config do aplicativo, definindo o tipo de campo padrão para as chaves
# name = nome do aplicativo