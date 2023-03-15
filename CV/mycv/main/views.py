from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm


def index_ru(request):
    return render(request, 'main/index_ru.html')


def about_skills_ru(request):
    return render(request, 'main/aboutskills_ru.html')


def about_studies_ru(request):
    return render(request, 'main/aboutstudies_ru.html')


def about_additional_ru(request):
    return render(request, 'main/aboutadditional_ru.html')


def communication_ru(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved')
        else:
            error = 'Форма заполнена некорректно. Заполните все поля'

    form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'main/communication_ru.html', context)


def index_en(request):
    return render(request, 'main/index_en.html')


def about_skills_en(request):
    return render(request, 'main/aboutskills_en.html')


def about_studies_en(request):
    return render(request, 'main/aboutstudies_en.html')


def about_additional_en(request):
    return render(request, 'main/aboutadditional_en.html')


def communication_en(request):
    return render(request, 'main/communication_en.html')


def saved_ru(request):
    return render(request, 'main/saved.html')

