from django.views.generic import ListView, DetailView

from university.models import Lesson


class ListLesson(ListView):
    model = Lesson
    queryset = Lesson.objects.all()
    template_name = 'lesson/list.html'


class DetailLesson(DetailView):
    model = Lesson
    queryset = Lesson.objects.all()
    template_name = 'lesson/detail.html'
