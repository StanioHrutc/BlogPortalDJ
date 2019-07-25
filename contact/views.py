from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Contact
# Create your views here.



def contact(request):
    name     = ''
    sur_name = ''
    email    = ''
    part_msg = ''

    if request.method == 'POST':

        valid_counter = 0

        if len(request.POST['user_name']) > 2:
            valid_counter += 1
            name = request.POST['user_name']
        else:
            part_msg += 'Your name must contain 2 or more letters.'

        if len(request.POST['last_name']) > 2:
            valid_counter += 1
            sur_name       = request.POST['last_name']
        else:
            part_msg += 'Your last name must contain 2 or more letters.'

        if request.POST['user_email']:
            valid_counter += 1
            email          = request.POST['user_email']

        if valid_counter == 3:
            if Contact.objects.all().filter(email=email):
                part_msg = 'User with this email already registered!'
                messages.error(request, part_msg)
                return render(request=request,
                              template_name='contact/contact.html',
                              context={'name': name, 'sur_name': sur_name, 'email': ''})
            else:
                subscriber = Contact(name=name,
                                     sur_name=sur_name,
                                     email=email,
                                     is_subscribed=True)
                subscriber.save()
                messages.success(request, 'You are successfully subscribed on blog')
                return redirect('/')
        else:
            messages.error(request, part_msg)
            return render(request=request,
                          template_name='contact/contact.html',
                          context={'name': name, 'sur_name': sur_name, 'email': email})

    return render(request, 'contact/contact.html')

# TODO: create validation of user input in contact form
