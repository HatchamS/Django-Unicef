from datetime import datetime
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    cat_name = models.CharField(max_length=200, help_text='Nom de la catégorie')
    colorBorder = models.CharField(max_length=20, help_text='code hexa couleur', default="#000000")

    def __str__(self):
        return self.cat_name


class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, default="", blank=True,help_text='Ne pas remplir')
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    photoPresentation = RichTextUploadingField(default="", config_name="imageUpload")
    contenu = RichTextUploadingField()
    date = models.CharField(default=datetime.now().strftime("%d %b %Y"), max_length=100)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        self.slug = slugify(f"{self.titre}")
        super(Article, self).save(*args, **kwargs)
