from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from . import models
from . import serializers
from .forms import RegisterUserForm


# Чтобы у меня работали лайки и дизлайки нужно
# использовать базу данный postgresql.

# И чтобы поставить лайк или дизлай я использовал @action - дополнительные действия,
# и надо прейти на: http://127.0.0.1:8000/api/v1/tweet или comment/pk/like или dislike/


class TweetViewSet(viewsets.ModelViewSet):
    queryset = models.Tweet.objects.all()
    serializer_class = serializers.TweetSerialize

    def get_queryset(self):
        return models.Tweet.objects.all().select_related('user')

    @action(methods=['get'], detail=True)
    def like(self, request, pk=None):
        tweet = get_object_or_404(models.Tweet, pk=pk)
        if request.user.id not in tweet.previous_users:
            tweet.alreadyLiked = False
            tweet.alreadyDisliked = False
            tweet.previous_users.append(request.user.id)
            tweet.save()
        if not request.user.is_authenticated:
            return Response('Not have access!')
        if not tweet.alreadyLiked:
            tweet.like += 1
            tweet.dislike -= 1
            tweet.alreadyLiked=True
            tweet.alreadyDisliked=False
            tweet.save()
        return Response({'like': tweet.like, 'dislike': tweet.dislike})

    @action(methods=['get'], detail=True)
    def dislike(self, request, pk=None):
        tweet = get_object_or_404(models.Tweet, pk=pk)
        if request.user.id not in tweet.previous_users:
            tweet.alreadyLiked=False
            tweet.alreadyDisliked=False
            tweet.previous_users.append(request.user.id)
            tweet.save()
        if not request.user.is_authenticated:
            return Response('Not have access!')
        if not tweet.alreadyDisliked:
            tweet.dislike += 1
            tweet.like -= 1
            tweet.alreadyDisliked=True
            tweet.alreadyLiked=False
            tweet.save()
        return Response({'like': tweet.like, 'dislike': tweet.dislike})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerialize

    def get_queryset(self):
        return models.Comment.objects.all().select_related('user')

    @action(methods=['get'], detail=True)
    def like(self, request, pk=None):
        comment = get_object_or_404(models.Comment, pk=pk)
        if request.user.id not in comment.previous_users:
            comment.alreadyLiked = False
            comment.alreadyDisliked = False
            comment.previous_users.append(request.user.id)
            comment.save()
        if not request.user.is_authenticated:
            return Response('Not have access!')
        if not comment.alreadyLiked:
            comment.like += 1
            comment.dislike -= 1
            comment.alreadyLiked = True
            comment.alreadyDisliked = False
            comment.save()
        return Response({'like': comment.like, 'dislike': comment.dislike})

    @action(methods=['get'], detail=True)
    def dislike(self, request, pk=None):
        comment = get_object_or_404(models.Comment, pk=pk)
        if request.user.id not in comment.previous_users:
            comment.alreadyLiked = False
            comment.alreadyDisliked = False
            comment.previous_users.append(request.user.id)
            comment.save()
        if not request.user.is_authenticated:
            return Response('Not have access!')
        if not comment.alreadyDisliked:
            comment.dislike += 1
            comment.like -= 1
            comment.alreadyDisliked = True
            comment.alreadyLiked = False
            comment.save()
        return Response({'like': comment.like, 'dislike': comment.dislike})


class RegisterUser(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/api/v1/tweet/')


