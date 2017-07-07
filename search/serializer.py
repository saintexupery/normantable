from rest_framework import serializers

from search.models import SearchWord


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchWord
        exclude = ('created_at', )

    def create(self, validated_data):
        search_word = validated_data['search_word']
        engine = validated_data['engine']

        search_obj = SearchWord(
            search_word = search_word,
            engine = engine,
        )
        search_obj.save()

        return search_obj
