## First run

Restful API vytvorené požitím Python (Django)

### Použité knižnice

* Django rest frameword

>pip install djangorestframework

Následne je to potrebné registrovať ako INSTALLED_APPS v settings.

### Príspevky

Príspevky majú normálny formát JSON, ale nezhodujú sa s Django serilization format. Tym pádom nebolo možné vložit do db systému príspevky s:

> python manage.py loaddata /utils/posts.json

Bolo by potrebné pridať: model & pk. (Som presvedčený, že môže byť aj iná možnosť), ale riešil som to nasledovne:

* V priečinku *utils*, je súbor *get_data_from_endpoint.py*,ktorý vloží do db všetky príspevky pri spustení.

### Spustenie

#### Vytvoriť migrations

> python manage.py makemigrations

#### Migrate

> python manage.py migrate

#### Spustiť

> python manage.py runserver

### Endpoints

all_posts/

* Slúži na zobrazenie príspevkov

add_post/

* Slúži na pridávanie príspevku

post_details/<int:id> napriklad post_details/1

* Slúžii na zobrazenie konkrétneho príspevku, následne aj na opravu aj vymazanie (záleží na používanej metóde- GET, PUT, DELETE)