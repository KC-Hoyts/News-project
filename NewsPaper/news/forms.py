from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django.utils.translation import gettext as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'post_category',
            'title',
            'text',

        ]

    #добавил сортировку категорий по алфавиту, на странице создания поста, чтоб было эстетичненько
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)
        self.fields['post_category'].queryset = self.fields['post_category'].queryset.order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        #здесь и ниже указываем параметры которые хотим проверять. Заготовка  = cleaned_data.get("")
        author = cleaned_data.get("author")
        categoryType = cleaned_data.get("categoryType")
        post_category= cleaned_data.get("post_category")
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        #  здесь и ниже указываем условия проверки
        if title == text:
            raise ValidationError("Текст статьи не должен равняться заголовку!")

        if title[0].islower() or len(title) > 30:
            raise ValidationError(
                "Название должно начинаться с заглавной буквы и не должно быть длиннее 30 символов"
            )

        #после всех манипулиций возвращаем "проверенные" данные с помощью return
        return cleaned_data

class Post_ar_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'post_category',
            'title',
            'text',

        ]

    #добавил сортировку категорий по алфавиту, на странице создания поста, чтоб было эстетичненько
    def __init__(self, *args, **kwargs):
        super(Post_ar_Form, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)
        self.fields['post_category'].queryset = self.fields['post_category'].queryset.order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        #здесь и ниже указываем параметры которые хотим проверять. Заготовка  = cleaned_data.get("")
        author = cleaned_data.get("author")
        categoryType = cleaned_data.get("categoryType")
        post_category= cleaned_data.get("post_category")
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        #  здесь и ниже указываем условия проверки
        if title == text:
            raise ValidationError("Текст статьи не должен равняться заголовку!")

        if title[0].islower() or len(title) > 40:
            raise ValidationError(
                "Название должно начинаться с заглавной буквы и не должно быть длиннее 40 символов"
            )

        if len(text) < 50 and categoryType == 'AR':
            raise ValidationError('Количество контекста слишком мало для статьи. Смените категорию на "Новость"')

        #после всех манипулиций возвращаем "проверенные" данные с помощью return
        return cleaned_data