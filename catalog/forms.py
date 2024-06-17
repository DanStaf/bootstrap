from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    #  Наследуемся от специального класса форм, который предоставляет
    #  весь необходимый функционал, который нужно настроить
    class Meta:
        model = Product  # Обязательно указываем модель
        fields = '__all__'  # и перечисляем поля для отображения

        """fields = '__all__'  # Использование всех полей модели
        fields = ('first_name',)  # Использование только перечисленных полей
        exclude = ('last_name',)  # Использование всех полей, кроме перечисленных
        # Описан может быть только один из вариантов"""

    def validate_my_text(self, field_name, error_text):

        forbidden_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]

        cleaned_data = self.cleaned_data.get(field_name)

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(error_text + f': ("{word}")')

        return cleaned_data

    def clean_name(self):
        return self.validate_my_text('name', 'Ошибка, связанная с названием Продукта')

    def clean_description(self):
        return self.validate_my_text('description', 'Ошибка, связанная с описанием Продукта')
