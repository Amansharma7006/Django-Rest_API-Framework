from rest_framework import serializers
from .models import Article


#         "By using ModelSerializer"
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Article
        fields= ['id','title','author','email']














#------------------------------------------------------------------
#        "by using simple serializer"

#class ArticleSerializer(serializers.Serializer):
#    title=serializers.CharField(max_length=50)
#    author=serializers.CharField(max_length=50)
#    email=serializers.EmailField(max_length=50)
#    date=serializers.DateTimeField()
#

#    def create(self,validated_data):
#        return Article.Objects.create(validated_data)
#
#    def update(self, instance,validated_data):
#        instance.title=validated_data.get('title',instance.title)
#        instance.author=validated_data.get('author',instance.author)
#        instance.email=validated_data.get('email',instance.email)
#        instance.save()
#        return instance
