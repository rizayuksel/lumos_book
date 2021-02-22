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

komutunu kullanarak oluşturabilirsiniz.


## KULLANILAN TEKNOLOJİLER
- **Dil:** Python
- **Framework:** Django
- **Veri Tabanı:** PostgreSQL
- **Search:** Elasticsearch
- **Front-End:** Bootstrap
- **Diğer:** Docker, Crispy Forms, ORM, ITBook Store API.


## EKRAN GÖRÜNTÜLERİ

#### 1. Ana Sayfa 
Tüm kitapların listelendiği sayfa.
![ana sayfa 1](https://user-images.githubusercontent.com/52426752/108761270-b1c8c580-755f-11eb-87c5-a665d73d86d3.PNG)
Kullanıcı girişi yaptıktan sonra istediğiniz kitabı bookmark listenize ekleyebilir, silebilirsiniz.
![ana sayfa 2](https://user-images.githubusercontent.com/52426752/108761655-2996f000-7560-11eb-8ae7-b7df2df5637b.PNG)

#### 2. Kitap Detayları
Kitapları bu sayfada inceleyebilirsiniz. Beğendiğiniz kitabı bookmark listenize ekleyebilir, silebilirsiniz.
![detay](https://user-images.githubusercontent.com/52426752/108761743-43d0ce00-7560-11eb-9623-e556e59da3c0.PNG)

#### 3. Profil
Bookmark listeniz burada listelenir. İstediğiniz kitabı listeden kaldırabilirsiniz.
![profil](https://user-images.githubusercontent.com/52426752/108761985-99a57600-7560-11eb-9009-3aa210758e08.PNG)

#### 4. Site Üzerinde Arama Sonuçları
Arama çubuğunda kitabın ismini, yazarını ya da isbn13 kodunu aratabilirsiniz. Arama yapısında *Elasticsearch* teknolojisi kullanılmıştır.
![arama](https://user-images.githubusercontent.com/52426752/108762006-9f02c080-7560-11eb-9c76-8cdb06a02b57.PNG)

#### 5. Sign Up
Gerekli bilgileri girerek siteye kayıt olabilirsiniz.
![kayıt ol](https://user-images.githubusercontent.com/52426752/108762017-a1651a80-7560-11eb-8b36-08cc3b360342.PNG)

#### 6. Login
Hesabınızla siteye giriş yapabilirsiniz.
![giriş yap](https://user-images.githubusercontent.com/52426752/108762030-a3c77480-7560-11eb-8fc0-67425d9ef88c.PNG)


## SON OLARAK
- **LUMOS:** Harry Potter'da asanın ucunda ışık belirmesini sağlayan büyü :)
