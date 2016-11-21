from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import MailFormAsker
from .forms import MailFormTasker
from django.shortcuts import redirect

def index(request):
    if request.method == "POST":
        if 'userbutton' in request.POST:
            form = MailFormAsker(request.POST)
        elif 'offerbutton' in request.POST:
            form = MailFormTasker(request.POST)

        if form.is_valid():
            mail = form.save(commit=False)
            mail.service = ", ".join( request.service )
            mail.save()
            return redirect('/', pk=mail.pk)
        else:
            asker_form=MailFormAsker(initial={'user_type': 'A'})
            tasker_form=MailFormTasker(initial={'user_type': 'T'})
    else:
        asker_form=MailFormAsker(initial={'user_type': 'A'})
        tasker_form=MailFormTasker(initial={'user_type': 'T'})
    return render(request, 'index.html', {'asker_form': asker_form, 'tasker_form': tasker_form})