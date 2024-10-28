from django.contrib import admin

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

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(FreeTemplate)
admin.site.register(WebDesine)
admin.site.register(Portfolio)
admin.site.register(Stories)
admin.site.register(ResentBlogMain)
admin.site.register(ResentComments)
admin.site.register(ResentPosts)
admin.site.register(Blogroll)
admin.site.register(ContactSocials)
admin.site.register(AboutTitles)
admin.site.register(AboutText1)
admin.site.register(AboutText1list)
admin.site.register(AboutText2)
admin.site.register(CategoriesMain)
admin.site.register(Categories)
admin.site.register(Testimonial)