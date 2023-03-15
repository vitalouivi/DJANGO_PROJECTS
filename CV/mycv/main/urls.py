from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_ru, name='homeru'),
    path('about-studies-ru', views.about_studies_ru, name='studru'),
    path('about-skills-ru', views.about_skills_ru, name='skillsru'),
    path('about-additional-ru', views.about_additional_ru, name='addru'),
    path('text-me-ru', views.communication_ru, name='commru'),

    path('index-en', views.index_en, name='homeen'),
    path('about-studies-en', views.about_studies_en, name='studen'),
    path('about-skills-en', views.about_skills_en, name='skillsen'),
    path('about-additional-en', views.about_additional_en, name='adden'),
    path('text-me-en', views.communication_en, name='commen'),

    path('form-saved', views.saved_ru, name='saved'),
]
