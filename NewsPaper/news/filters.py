from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateTimeFilter, CharFilter, ChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category

class PostFilter(FilterSet):
    post_category = ModelMultipleChoiceFilter(
        field_name="postcategory__categoryThrough", #имя промежуточной/конечной модели__атрибут
        queryset=Category.objects.all(),
        label="Категория",
        conjoined = True

    )

    title = CharFilter(
        field_name="title",  # имя промежуточной/конечной модели__атрибут
        label="Заголовок",
        lookup_expr='icontains',

    )

    categoryType = ChoiceFilter(choices=Post.CATEGORY_CHOISES, label='Тип публикации')

    added_after = DateTimeFilter(
        field_name='date_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'},
        ),
        label='Дата и время публикации'
    )

    # class Meta:
    #     model = Post
    #     fields = [
    #         'titles',
    #         'categorys',
    #         'category_type',
    #         'added_after'
    #
    #     ]
