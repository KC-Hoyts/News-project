from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy # импортируем «ленивый» геттекст с подсказкой

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):

    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser}'


    def update_raiting(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()



class Post(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               verbose_name=pgettext_lazy('Выпадающий список авторов', 'Автор'))

    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOISES = [
        (NEWS, "Новость"),
        (ARTICLE, "Статья")
    ]

    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=ARTICLE)
    date_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through="PostCategory",
                                           verbose_name=pgettext_lazy('Список категорий', 'Категория'))
    title = models.CharField(max_length=128, verbose_name=pgettext_lazy('Ввод заголовка', 'Заголовок'))
    text = models.TextField(verbose_name=pgettext_lazy('Ввод текста поста', 'Текст поста'))
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:128] + '...'



    # def __str__(self):
    #     return f'|{self.title}: {self.text[:15]}...|'

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
        

