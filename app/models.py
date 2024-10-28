from django.db import models


class HeaderText(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"

 
class FooterText(models.Model):
    text = models.CharField(max_length=255)
    link_url = models.URLField(max_length=255)
    link_name = models.CharField(max_length=255)
 


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"



class FreeTemplate(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    description3 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=255)
    link_name = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Free Template"
        verbose_name_plural = "Free Template"



class WebDesine(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    list1 = models.CharField(max_length=255, blank=True, null=True)
    list2 = models.CharField(max_length=255, blank=True, null=True)
    list3 = models.CharField(max_length=255, blank=True, null=True)
    list4 = models.CharField(max_length=255, blank=True, null=True)
    list5 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Web Desine"
        verbose_name_plural = "Web Desine"



class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_class = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="portfolio.url", blank=True, null=True)
   
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"



class Stories(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="stories.url", blank=True, null=True)
   
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Stories"
        verbose_name_plural = "Stories"



class ResentBlogMain(models.Model):
    title = models.CharField(max_length=255)
  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Resent Blog Main"
        verbose_name_plural = "Resent Blog Main"



class ResentPosts(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
 


    def __str__(self):
        return f"{self.link_name}"

    class Meta:
        verbose_name = "Resent Posts"
        verbose_name_plural = "Resent Posts"



class ResentComments(models.Model):
    link_url1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return f"{self.link_name1}"

    class Meta:
        verbose_name = "Resent Comments"
        verbose_name_plural = "Resent Comments"



class Blogroll(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)

    def __str__(self):
            return f"{self.link_name}"

    class Meta:
        verbose_name = "Blogroll"
        verbose_name_plural = "Blogroll"


class ContactSocials(models.Model):
    title = models.CharField(max_length=255)
    link_url = models.URLField(max_length=255)
    link_name = models.CharField(max_length=255)
    class_link = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Socials"
        verbose_name_plural = "Contact Socials"



class AboutTitles(models.Model):
    title = models.CharField(max_length=255)
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Titles"
        verbose_name_plural = "About Titles"



class AboutText1(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
    description3 = models.CharField(max_length=500, blank=True, null=True)
    link_url1 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Text1"
        verbose_name_plural = "About Text1"  


class AboutText1list(models.Model):
    list_name = models.CharField(max_length=255)

    def __str__(self):
        return self.list_name

    class Meta:
        verbose_name = "About Text1 List"
        verbose_name_plural = "About Text1 List"         
        


class AboutText2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link_url1 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(max_length=255, blank=True, null=True)
    blockquote = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Text2"
        verbose_name_plural = "About Text2"



class CategoriesMain(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categories Main"
        verbose_name_plural = "Categories Main"         
        



class Categories(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.link_name}"

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"         
        				


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"
