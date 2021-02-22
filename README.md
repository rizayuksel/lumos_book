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
