from django.urls import path

from university.views import ListLesson, DetailLesson


app_name = 'university'

urlpatterns = [
    path('lesson/', ListLesson.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', DetailLesson.as_view(), name='lesson-detail'),
]
