from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    FreeTemplate,
    WebDesine,
    Portfolio,
    Stories,
    ResentBlogMain,
    ResentComments,
    ResentPosts,
    ResentComments,
    Blogroll,
    ContactSocials,
    AboutTitles,
    AboutText1,
    AboutText1list,
    AboutText2,
    CategoriesMain,
    Categories,
    Testimonial
    )



def index(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "free_template": FreeTemplate.objects.all().first(),
        "web_desine": WebDesine.objects.all().first(),
        "portfolio": Portfolio.objects.all().first(),
        "stories": Stories.objects.all(),
        "resent_blog_main": ResentBlogMain.objects.all(),
        "resent_posts": ResentPosts.objects.all(),
        "resent_comments": ResentComments.objects.all(),
        "blogroll": Blogroll.objects.all(),
        "contact_socials": ContactSocials.objects.all()

   }
    
    return render(request,"home.html", context)

def about(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "about_text1": AboutText1.objects.all().first(),
        "about_text1_list": AboutText1list.objects.all(),
        "about_text2": AboutText2.objects.all().first(),
        "about_titles": AboutTitles.objects.all().first(),
        "categories_main": CategoriesMain.objects.all().first(),
        "categories": Categories.objects.all(),
        "testimonial": Testimonial.objects.all().first(),
        "categories": Categories.objects.all(),
        "resent_blog_main": ResentBlogMain.objects.all(),
        "resent_posts": ResentPosts.objects.all(),
        "resent_comments": ResentComments.objects.all(),
        "blogroll": Blogroll.objects.all(),
        "contact_socials": ContactSocials.objects.all()
    }
    
    return render(request, "about.html", context)

def contact(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "categories_main": CategoriesMain.objects.all().first(),
        "categories": Categories.objects.all(),
        "testimonial": Testimonial.objects.all().first(),
        "categories": Categories.objects.all(),
        "resent_blog_main": ResentBlogMain.objects.all(),
        "resent_posts": ResentPosts.objects.all(),
        "resent_comments": ResentComments.objects.all(),
        "blogroll": Blogroll.objects.all(),
        "contact_socials": ContactSocials.objects.all()
    }
    
    return render(request, "contact.html", context)


def blog(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "categories_main": CategoriesMain.objects.all().first(),
        "categories": Categories.objects.all(),
        "testimonial": Testimonial.objects.all().first(),
        "categories": Categories.objects.all(),
        "resent_blog_main": ResentBlogMain.objects.all(),
        "resent_posts": ResentPosts.objects.all(),
        "resent_comments": ResentComments.objects.all(),
        "blogroll": Blogroll.objects.all(),
        "contact_socials": ContactSocials.objects.all()
    }
    
    return render(request, "blog.html", context)



def blog_post(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    
    return render(request, "blog_post.html", context)


def flash_slider(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    
    return render(request, "flash_slider.html", context)


def portfolio(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "resent_blog_main": ResentBlogMain.objects.all(),
        "resent_posts": ResentPosts.objects.all(),
        "resent_comments": ResentComments.objects.all(),
        "blogroll": Blogroll.objects.all(),
        "contact_socials": ContactSocials.objects.all()
    }
    
    return render(request, "portfolio.html", context)