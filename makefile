.PHONY: run
run:
	 python manage.py runserver

.PHONY: migrations
migrations:
	 python manage.py makemigrations

.PHONY: migrate
migrate: 
	python manage.py migrate

.PHONY: superuser
superuser: 
	python manage.py createsuperuser


.PHONY: combined
combined: migrations migrate ;

.PHONY: test
tests: 
	python manage.py test base.test