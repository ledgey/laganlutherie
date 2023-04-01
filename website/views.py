from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']} \nEmail: {form.cleaned_data['email']} \n\n{form.cleaned_data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@laganlutherie.com']
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('home')

    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})


def pricing(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']} \nEmail: {form.cleaned_data['email']} \n\n{form.cleaned_data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@laganlutherie.com']
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('pricing')
    else:
        form = ContactForm()
    return render(request, 'pricing.html', {'form': form})


def about(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']} \nEmail: {form.cleaned_data['email']} \n\n{form.cleaned_data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@laganlutherie.com']
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'form': form})


def services(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']} \nEmail: {form.cleaned_data['email']} \n\n{form.cleaned_data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@laganlutherie.com']
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('services')
    else:
        form = ContactForm()
    return render(request, 'services.html', {'form': form})