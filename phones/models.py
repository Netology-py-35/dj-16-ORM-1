from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    # Мне кажется эта строка не имеет смысла, так как id primary_key
    # устанавливается автоматически если нигде далее он не указан.
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                blank=True,
                                null=True)
    image = models.ImageField()
    release_date = models.TextField()
    lte_exists = models.BooleanField(blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)


#
# Что необходимо сделать: * В файле `models.py` нашего приложения создаем модель Phone с полями `id`, `name`,
# `price`, `image`, `release_date`, `lte_exists` и `slug`. Поле `id` - должно быть основным ключом модели. * Значение
# поля `slug` должно устанавливаться слагифицированным значением поля `name`. * Написать скрипт для переноса данных
# из csv-файла в модель `Phone`. Скрипт необходимо разместить в файле `import_phones.py` в методе `handle(self,
# *args, **options)` * При запросе `<имя_сайта>/catalog` - должна открываться страница с отображением всех телефонов.
# * При запросе `<имя_сайта>/catalog/iphone-x` - должна открываться страница с отображением информации по телефону. *
# В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию (в алфавитном порядке) и
# по цене (по-убыванию и по-возрастанию).
