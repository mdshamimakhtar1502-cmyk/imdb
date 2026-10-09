from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','description','active']
    
    def validate_name(self, data):
        if len(data) < 2:
            raise serializers.ValidationError('name is too short')
        else:
            return data


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    # def create(self,validated_data):
    #     return Movie.objects.create(**validated_data)