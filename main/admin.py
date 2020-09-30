from django.contrib import admin
from .models import Slide, Categorie_produit, Categories_Solution, SliderAPropos, Catalogue, ContactForm, Partenaire, Produit, ProduitDetail, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name',)
    list_per_page = 40
    list_filter = ('name',)
    search_fields = ('id', 'name',)

class SolutionCategoryAdmin(CategoryAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id','name', 'active')
    list_display_links = ('id', 'name')
    list_editable = ('active',)

class SliderAProposAdmin(CategoryAdmin):
    pass

class CatalogueAdmin(CategoryAdmin):
    list_display = ('id','name', 'categorie')
    list_filter = ('name', 'categorie',)

class ContactFormAdmin(CategoryAdmin):
    list_display = ('id','name', 'date_added', 'departement')
    readonly_fields = ('date_added',)

class PartenairesAdmin(CategoryAdmin):
    pass

class ProduitAdmin(CategoryAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProduitDetailAdmin(CategoryAdmin):
    list_display = ('id','name', 'gamme')
    list_filter = ('gamme',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titre')
    list_display_links = ('id','titre',)
    prepopulated_fields = {"slug": ("titre",)}



admin.site.register(Slide, CategoryAdmin)
admin.site.register(Categorie_produit, CategoryAdmin)
admin.site.register(Categories_Solution, SolutionCategoryAdmin)
admin.site.register(SliderAPropos, SliderAProposAdmin)
admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Partenaire, PartenairesAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(ProduitDetail, ProduitDetailAdmin)
admin.site.register(Post, PostAdmin)