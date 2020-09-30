from django.db import models
from django.urls import reverse
from django.utils import timezone

from ckeditor.fields import RichTextField
# Create your models here.
class Slide(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length= 200, blank = True)
    image = models.ImageField(upload_to= 'slides/')
    class Meta:
        verbose_name = "Photo page d'accueil"
        verbose_name_plural = "Photos page d'accueil"

    


class Categorie_produit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank= True)
    image = models.FileField(upload_to='slides/', blank= True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalogue", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Catégorie produit'
        verbose_name_plural = 'Catégories produits'

class Produit(models.Model):
    name        = models.CharField( max_length=50)
    slug        = models.SlugField( max_length=70)
    titre       = models.CharField( max_length=50, blank= True)
    gamme       = models.ForeignKey("Categorie_produit", verbose_name=("catégorie gamme"), on_delete=models.CASCADE)
    sous_titre  = models.CharField(max_length=100, verbose_name=("Sous titre"), blank= True)
    description  = models.TextField(blank= True)
    image       = models.FileField(upload_to='slides/', blank= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produits'
        verbose_name_plural = 'Produits'


class ProduitDetail(models.Model):
    name        = models.CharField(max_length=50)
    gamme       = models.ForeignKey("Produit", verbose_name=("catégorie gamme"), on_delete=models.CASCADE)
    image       = models.FileField(upload_to='slides/', blank= True)
    def __str__(self):
        return  self.name

    def __unicode__(self):
        return 



class Categories_Solution(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, blank=True)
    
    text1 = models.TextField(verbose_name='Grand titre' ,blank= True)
    image = models.ImageField(verbose_name='Image principale' ,upload_to='slides/', blank= True)
    image2 = models.ImageField(upload_to='slides/', blank= True)
    description = models.TextField(blank= True)
    text2 = RichTextField(verbose_name='Text en plus', blank= True, null=True)
    active = models.BooleanField(default=True)



    class Meta:
        verbose_name = 'solution'
        verbose_name_plural = 'solutions'


class SliderAPropos(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slides/')

    class Meta:
        verbose_name = 'photo page a propos'
        verbose_name_plural = 'photos page a propos'


class Catalogue(models.Model):
    categorie = models.ForeignKey("Categorie_produit", verbose_name=("catégorie"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slides/')
    description = models.TextField(blank= True)

#     # def get_absolute_url(self):
#     #     # return reverse("gamme", kwargs={'id': self.id, 'categorie_id': self.categorie_id})
#     #     return "/catalogue/%i/" %self.id
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'gamme'
        verbose_name_plural = 'catalogue'

DEPARTEMENT_CHOICES=[
    ('C', 'Commercial'),
    ('D', 'Direction'),
    ('M', 'Marketing'),
    ('SC', 'Service client'),
    ]
class ContactForm(models.Model):
    name        = models.CharField(max_length=50)
    departement = models.CharField(max_length=2, choices=DEPARTEMENT_CHOICES, default='D',)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20)
    subject     = models.CharField(max_length=50)
    fichier     = models.FileField(upload_to='fichiers/% d/% m/% Y/', max_length=20, blank=True)
    message     = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Formulaire de contact'

class Partenaire(models.Model):
    name= models.CharField( max_length=50)
    logo = models.ImageField(upload_to='part/')
    url_marque = models.URLField(max_length=200, blank=True) 

    def __str__(self):
        return self.name

class Post(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    intro = models.CharField(max_length=200, blank=True)
    image = models.ImageField(verbose_name='Image' ,upload_to='slides/', blank= True)
    text = RichTextField(verbose_name='Article', blank= True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titre