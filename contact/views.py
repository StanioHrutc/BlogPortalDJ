from django.shortcuts import render, redirect

from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        name     = request.POST['user_name']
        sur_name = request.POST['last_name']
        email    = request.POST['user_email']

        subscriber = Contact(name=name, sur_name=sur_name, email=email, is_subscribed=True)

        subscriber.save()

        return redirect('/')

    return render(request, 'contact/contact.html')
