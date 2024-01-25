from django import forms
from .models import Comments

# Форма для модели Comments.
# Форма будет содержать поля "name" и "text_comments", которые пользователь будет заполнять при отправке комментария.
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text_comments')