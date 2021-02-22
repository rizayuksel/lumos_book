# LUMOS BOOK

## PROJEYİ ÇALIŞTIRMAK İÇİN;

Bu git repo'sunu bilgisayarınızda bir klasöre indirin. Klasörde docker-compose dosyasının bulunduğu dizinde terminal açıp sırasıyla, 

```
docker-compose build

docker-compose up
```

komutlarını çalıştırın. Gerekli indirmeler tamamlandıktan sonra browser'da **localhost:8000**'de projeyi açabilirsiniz. Eğer bir superuser oluşturmak isterseniz, aynı dizinde

```
docker-compose run web python manage.py createsuperuser
```

komutuyla oluşturabilirsiniz.


## KULLANILAN TEKNOLOJİLER
**Dil:** Python
**Framework:** Django
**Veri Tabanı:** PostgreSQL
**Search:** Elasticsearch
**Front-End:** Bootstrap
**Diğer:** Docker, Crispy Forms, ORM, ITBook Store API.


## EKRAN GÖRÜNTÜLERİ

#### Ana Sayfa 
https://user-images.githubusercontent.com/52426752/108761270-b1c8c580-755f-11eb-87c5-a665d73d86d3.PNG
