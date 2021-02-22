from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import SearchTable

#This page for elasticsearch. Connecting to our searchtable and pull all the data.

@registry.register_document
class SearchBookDocument(Document):
    class Index:
        name = 'search'
        settings = {'number_of_shards': 1, 
                    'number_of_replicas': 0}

    class Django:
        model = SearchTable 

        fields = [
            'id',
            'title',
            'author',
            'isbn13',
            'image',
            'keyword',
        ]