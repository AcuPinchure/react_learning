from django.urls import path, include
from . import views, api_views
from rest_framework.routers import DefaultRouter

app_name = 'todo'

router = DefaultRouter()
router.register('todos', api_views.TodoViewSet)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('api/', include(router.urls)),
]
