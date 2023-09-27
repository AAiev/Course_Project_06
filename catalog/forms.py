from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price',)
        # exclude = ('date_create', 'date_last_modified',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        unacceptable_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in unacceptable_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимое название продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        unacceptable_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in unacceptable_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимое описание продукта')

        return cleaned_data