# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TabForm
from .models import Tab
from django.shortcuts import get_object_or_404
from .filters import TabFilter
from django.core.paginator import Paginator



def all_tabs(request):
    all_tabs=Tab.objects.all()
    snippets=Tab.objects.all()[1:5]


    myFilter = TabFilter(request.GET, queryset=all_tabs)
    all_tabs = myFilter.qs
    
    paginator = Paginator(all_tabs, 5) # Show 25 items per page
    page = request.GET.get('page')
    all_tabs = paginator.get_page(page)

    context={
        'all_tabs': all_tabs,
        'snippets': snippets,
    }
    return render(request, 'tab_index2.html',  context)


def tabs(request):
    tabs = Tab.objects.all().order_by('-created_at')
    most_recent = Tab.objects.order_by('-created_at')[:6]
    # featured = Tab.objects.filter(featured=True)
    myFilter = TabFilter(request.GET, queryset=tabs)
    tabs = myFilter.qs
    
    paginator = Paginator(tabs, 5) # Show 25 items per page
    page = request.GET.get('page')
    tabs = paginator.get_page(page)

    context = {
        'tabs': tabs,
        "myFilter": myFilter,
        'most_recent': most_recent,
        # 'featured': featured,
        
        # 'header_news': header_news,
        # 'snippets': snippets,
        # 'top5_categories': top5_categories
    }

    return render(request, 'tab_index.html', context)


def tab_detail(request, slug):
    print("slug", slug)
    tab = get_object_or_404(Tab, slug=slug)
    context = { "tab": tab }
    return render(request, 'tab_detail.html', context)

@login_required(login_url='login')
def create_tab(request):
    tabs = Tab.objects.all().order_by('-created_at')[:10]
    
    if request.method == 'POST':
        form = TabForm(request.POST)
        if form.is_valid():
            tab = form.save(commit=False)
            tab.author = request.user
            tab.save()
            return redirect('tab_index')
    else:
        form = TabForm()
        
        
    context = {
        'form': form,
        'tabs': tabs
    }

        
        
    return render(request, 'create_tab.html', context)


def error_404(request, exception):
    return render(request, "404.html")




def tab_category(request, category):
    posts = Tab.objects.filter(categories__name__contains=category).order_by('-created_at')

    context = {
        "category": category,
        "tabs": tabs,
    }
    return render(request, "tab_category.html", context)
