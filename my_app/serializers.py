from rest_framework import serializers

from . import models


class TweetSerialize(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Tweet
        fields = ('title', 'text', 'like', 'dislike', 'user')
        read_only_fields = ('like', 'dislike')


class CommentSerialize(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Comment
        fields = ('comment', 'like', 'dislike', 'tweet', 'user')
        read_only_fields = ('like', 'dislike')
