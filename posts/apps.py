""" Post aplication module """
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post aplication settings """
    name = 'posts'

    #nombre de nuesta app pero en bonito
    verbose_name = 'Posts'
