from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add_post/', views.add_post),
    path('all_posts/', views.get_all_posts),
    path('post_details/<int:id>', views.post_details),
    path('dj_front/', views.dj_front_home, name='posts'),
    path('dj_front/<int:id>', views.dj_front_detail, name='post_detail')
]