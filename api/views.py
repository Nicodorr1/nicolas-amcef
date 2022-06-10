from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
import requests

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def add_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        checking_user = requests.get('https://jsonplaceholder.typicode.com/users').json()
        for user in checking_user:
            if serializer.validated_data.get('userId') == user['id']:
                print("User exists, ready to go.. ")
                serializer.save()
                return Response({"Status": "Post added"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Status": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Get'])
def get_all_posts(request):
    q = Post.objects.all()
    serializer = PostSerializer(q, many=True)
    # pemission_classes = [permissions.IsAuthenticated]
    return Response(serializer.data)


@api_view(['Get', 'PUT', 'DELETE'])
def post_details(request, id):

    try:
        post = Post.objects.get(pk=id)
        try_with_filter = Post.objects.filter(pk=id)
    except Post.DoesNotExist:
        try_with_filter = Post.objects.filter(pk=id)
        if try_with_filter:
            print("exitst")
        else:
            try:
                checking = requests.get('https://jsonplaceholder.typicode.com/posts').json()
                print("Cheking...")

                for dt in checking:
                    if dt['id'] == id:
                        print("Post exist online - add it to your db")

                        foundId = dt['id']
                        foundUserId = dt['userId']
                        foundTitle = dt['title']
                        foundBody = dt['body']

                        foundData = Post(id=foundId, userId=foundUserId, title=foundTitle, body=foundBody)

                        save_d = foundData.save()
                        if save_d:
                            return Response(status=status.HTTP_202_ACCEPTED)
                        else:
                            return Response(status=status.HTTP_400_BAD_REQUEST)

            except:
                print("Post not exist")

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            serializer.save(title=title, body=body)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Use templates to display
def dj_front_home(request):
    dj_posts = Post.objects.all().order_by('id')
    context = {
        'dj_posts': dj_posts
    }
    return render(request, 'posts.html', context)


def dj_front_detail(request, id):
    dj_post = Post.objects.get(id=id)

    context = {
        'dj_post': dj_post
    }

    return render(request, 'post_detail.html', context)