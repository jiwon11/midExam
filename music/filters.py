from django import forms
import django_filters
from music.models import Music


class MusicFilter(django_filters.FilterSet):
    class Meta:
        model = Music
        fields = {
            'music_name': ['startswith', ],
            'music_brand': ['startswith', ],
            'music_producer': ['startswith', ],
            'music_price': ['gt', 'range'],
            'music_quantity': ['gt', 'range'],
        }
