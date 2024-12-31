from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from .forms import LessonForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app/course_list.html', {'courses': courses})

def lesson_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    return render(request, 'app/lesson_list.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'app/lesson_detail.html', {'lesson': lesson})


def add_post(request, ):
    if request.method == 'POST':
        form = LessonForm(data=request.POST)
        if form.is_valid():
            lesson = Lesson.objects.create(
                **form.cleaned_data
            )
            return redirect('lesson_detail', lesson_id=lesson.id)

    form = LessonForm()
    context = {
        "form": form
    }
    return render(request, 'app/add_post.html', context)


def update_post(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.title = form.cleaned_data.get('title')
            lesson.content = form.cleaned_data.get('content')
            lesson.course = form.cleaned_data.get('course')
            lesson.save()
 
    form = LessonForm(initial={
        'title':lesson.title,
        'content':lesson.content,
        'course':lesson.course
    })

    context = {
        "form":form 
    }
    return render(request, 'app/add_post.html', context)
    