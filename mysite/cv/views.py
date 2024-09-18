from django.shortcuts import render
from .models import Education, Experience, Skill, Language


def cv_view(request):
    education_list = Education.objects.all()
    experience_list = Experience.objects.all()
    skills_list = Skill.objects.all()
    language_list = Language.objects.all()

    context = {
        "education_list": education_list,
        "experience_list": experience_list,
        "skills_list": skills_list,
        "language_list": language_list,
    }

    return render(request, "cv/cv.html", context)
