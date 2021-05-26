import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone_obj = Phone(id=line[0], name=line[1], image=line[2], price=line[3], release_date=line[4], lte_exists=line[5])
                phone_obj.save()


# ['1', 'Samsung Galaxy Edge 2', 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig', '73000', '2016-12-12', 'True', '']
# ['2', 'Iphone X', 'https://avatars.mds.yandex.net/get-mpic/200316/img_id270362589725797013.png/orig', '80000', '2017-06-01', 'True', '']
# ['3', 'Nokia 8', 'https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig', '20000', '2013-01-20', 'False', '']