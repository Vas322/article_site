from django.db import models
from django.utils import timezone
from datetime import datetime
from os.path import splitext
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField


def get_timestamp_path(instance, filename):
    """Функция генерирует имена картинок исходя из текущей даты"""
    return "%s%s" % (datetime.now().timestamp(), splitext(filename)[1])


class Article(models.Model):
    """Модель описывает статью"""
    title = models.CharField(max_length=200, verbose_name='Введите название статьи')
    text = RichTextUploadingField(verbose_name='', blank=True, config_name='default')
    created_date = models.DateTimeField(verbose_name='Дата создания статьи',
                                        default=timezone.now)
    image = models.ImageField(blank=True, upload_to=get_timestamp_path,
                              verbose_name='Загрузить изображение')

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 250:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Статьи' """
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_date']

