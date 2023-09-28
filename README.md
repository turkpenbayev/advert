# advert
Необходимо написать небольшое приложение на django и django_rest_framework

Модели:

Category - категории объявлений, поля: name<br />
City - город объявления, поля: name<br />
Advert - объявление, поля: created (дата создания), title, description, city, category, views

Вью:

/api/advert/ - json список объявлений со всеми полями + название города + название категории <br/>
/api/advert/\<advert-pk\>/ - json detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении

Создайте образы и запустите контейнеры:

```sh
docker-compose up -d --build
```

1. Документация [http://localhost:8000/docs](http://localhost:8000/docs)
1. Админка [http://localhost:8000/admin](http://localhost:8000/admin) 
```sh
username: admin
password: admin
```
