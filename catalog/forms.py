from django import forms

from catalog.models import Product, Version

class StyleFormMaxin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_key, field_value in self.fields.items():
            field_value.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMaxin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы регистрации"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['name'].widget.attrs.update({"placeholder": 'Введите название продукта'})
            self.fields['description'].widget.attrs.update({"placeholder": 'Введите описание продукта'})
            self.fields['category'].widget.attrs.update({"placeholder": 'Выбирите категорию'})

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price', )
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

class VersionForm(StyleFormMaxin, forms.ModelForm):
    class Meta:

        model = Version
        fields = ('name', 'number', 'attribute',)
