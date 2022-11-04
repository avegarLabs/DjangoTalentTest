from django.urls import path
from .views import MoviesViews

urlpatterns = [
    path('movies/', MoviesViews.as_view(),name='movies_list'),
    path('movies/<str:id>',MoviesViews.as_view(),name='movies_precess')
]
 