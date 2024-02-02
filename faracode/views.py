from django.shortcuts import render

from contactus_app.models import Footer, Message
from projects_app.models import Project


def home(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')
        Message.objects.create(fname=fname, email=email, sub=sub, body=body)

    projects = Project.objects.all()
    footers = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects': projects, 'footers': footers})
