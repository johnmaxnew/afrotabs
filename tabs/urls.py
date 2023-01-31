from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_tab, name="create_tab"),
    path('tabs/', views.tabs, name="tab_index"),
    path('tabs/<slug>/', views.tab_detail, name="detail"),
    path('tabs/all-tabs', views.all_tabs, name="all"),
]





