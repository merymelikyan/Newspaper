from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('blog_post/', views.blog_post, name="blog_post"),
    path('flash_slider/', views.flash_slider, name="flash_slider"),
    path('portfolio/', views.portfolio, name="portfolio"),
          
] 