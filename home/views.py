from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .filters import HomeFilter

from home.models import Home, About, Contact, Privacy, Terms, Cookie
from tabs.models import Tab

def home_index(request):
    home = Home.objects.all().order_by('-created_at')
    featured = Tab.objects.filter(featured=True)
    most_recent = Home.objects.order_by('-created_at')[:3]

    myFilter = HomeFilter(request.GET, queryset=home)
    home = myFilter.qs

    context = {
        'home': home,
        "myFilter": myFilter,
        'most_recent': most_recent,
        'featured': featured,
    }
    return render(request, 'home_index.html', context)


def home_index(request):
    model = Tab
    latest_tabs = Tab.objects.order_by('-created_at')[:3]


    context = {
        'latest_tabs': latest_tabs,
    }
    return render(request, 'home_index.html', context)

# def home_detail(request, slug):
#     home = Home.objects.get(slug=slug)
#     context = {
#         'home': home,
#     }
#     return render(request, 'home_detail.html', context)

def about(request):
    about = About.objects.get()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)

def cookie(request):
    cookie = Cookie.objects.get()
    context = {
        'cookie': cookie
    }
    return render(request, 'cookie.html', context)

def privacy(request):
    privacy = Privacy.objects.get()
    context = {
        'privacy': privacy
    }
    return render(request, 'privacy.html', context)

def terms(request):
    terms = Terms.objects.get()
    context = {
        'terms': terms
    }
    return render(request, 'terms.html', context)


def contact(request):
    contact = Contact.objects.get()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
        
        subject = request.POST.get('subject')
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(subject, message, email, ['testmail@gmail.com'], fail_silently=False)
        return redirect ("home")
    
    
    context = {
        'contact': contact,
        'form':form
    }
    return render(request, 'contact.html', context)
