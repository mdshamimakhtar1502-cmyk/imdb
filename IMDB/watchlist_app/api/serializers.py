from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        # fields = ['id','title','storyline','platform','active','created']
        fields = '__all__'
        


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie_detail')
    class Meta:
        model = StreamPlatform
        # fields = ['id','name','about','website']
        fields = '__all__'


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