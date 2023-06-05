from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm, Post_ar_Form
from django.urls import reverse_lazy


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'all_news.html'
    context_object_name = 'All_News'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        #print(f"ЭТО КОНТКСТ ========{context}=======")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class OneNews(DetailView):
    model = Post
    template_name = "one_news.html"
    context_object_name = "One_News"

class NewsSearch(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'news_search.html'
    context_object_name = 'News_search'
    paginate_by = NewsList.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        #print(f"ЭТО КОНТКСТ ========{context}=======")


        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

class PostCreate(CreateView):   # через класс объявляем форму создания НОВОСТИ
    form_class = PostForm    #используется класс джанго CreateView, (из коробки)
    model = Post            # также для этого класса переопределяем метод get_absolute_url в моделях
    template_name = "post_edit.html"


    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType = "NW"
        return super().form_valid(form)

class PostArCreate(CreateView):   # через класс объявляем форму создания СТАТЬИ
    form_class = Post_ar_Form    #используется класс джанго CreateView, (из коробки)
    model = Post            # также для этого класса переопределяем метод get_absolute_url в моделях
    template_name = "post_edit.html"


    def form_valid(self, form):
        article = form.save(commit=False)
        article.categoryType = "AR"
        return super().form_valid(form)



# а это создание страницы через функцию: (не забудь импортировать и указать в path в urls.py эту функцию на втором месте)
# def create_product(request):
#     form = ProductForm()
#
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/products/")
#
#     return render(request, "product_edit.html", {"form" : form})

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = "post_edit.html"


class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('post_list')

