from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


# Представление для отображения списка всех записей
class PostView(View):
    def get(self, request):
        # Получаем все записи из базы данных
        posts = Post.objects.all()
        # Отображаем список записей на странице
        return render(request, 'blog/blog.html', {'post_list': posts})


# Представление для отображения конкретной записи
class PostDetail(View):
    def get(self, request, pk):
        # Получаем конкретную запись по её id
        post = Post.objects.get(id = pk)
        # Отображаем конкретную запись уже на другой странице
        return render(request, 'blog/blog_detail.html', {'post': post})

# Представление для добавления комментария к конкретной записи
class AddComments(View):

    def post(self, request, pk):
        # Создаем форму на основе данных, полученных из POST-запроса
        form = CommentsForm(request.POST)
        # Проверяем, валидна ли форма
        if form.is_valid():
            # Создаем объект комментария, но не сохраняем его в базе данных пока
            form = form.save(commit=False)
            # Присваиваем комментарию id записи, к которой он относится
            form.post_id = pk
            # Сохраняем комментарий в базе данных
            form.save()
        # Перенаправляем пользователя обратно к записи, к которой он добавил комментарий
        return redirect(f'/{pk}')




