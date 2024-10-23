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
