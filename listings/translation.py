from modeltranslation.translator import translator, TranslationOptions
from .models import Listing


class ProductCategoryTranslationOptions(TranslationOptions):
   fields = ('description',)
	
translator.register(Listing, ProductCategoryTranslationOptions)