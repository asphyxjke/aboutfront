from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length= 200)
    description = models.TextField('Текст')
    author = models.CharField('Имя автора', max_length= 200)
    date = models.DateField('Дата')
    img = models.ImageField('Изображение', upload_to='image/', max_length=200, blank=True)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
#Функция обеспечивает читаемое представление для админки.
    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


