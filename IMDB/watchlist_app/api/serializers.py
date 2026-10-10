from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = ['id','name','about','website']


    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError('name should be different')
    #     else:
    #         return data
        
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('name is too short')
    #     else:
    #         return value



class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ['id','title','storyline','active','created']
        
    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError('name should be different')
    #     else:
    #         return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('name is too short')
    #     else:
    #         return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    # def create(self,validated_data):
    #     return Movie.objects.create(**validated_data)