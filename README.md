# resume

The goal of this project is to provide a simple application to build a resume and output it in various formats such as PDF, DOCX, JSON, etc.

This uses docker-compose to facilitate the development environment.

First run requires running migrations while the docker-compose containers are running.

`docker-compose up`

`docker-compose run web python3 manage.py makemigrations viewer && python3 manage.py sqlmigrate viewer 0001 && python3 manage.py migrate`

Landing Page:

![image](https://user-images.githubusercontent.com/46699116/73128862-04196a80-3f8b-11ea-8e7d-07aaa5a5acc1.png)

Admin:

![image](https://user-images.githubusercontent.com/46699116/73037863-5c266480-3e05-11ea-8f54-67eb9c6b0415.png)

HTML:

![image](https://user-images.githubusercontent.com/46699116/73037717-ea4e1b00-3e04-11ea-8dd1-317a8c0b7392.png)

JSON:

![image](https://user-images.githubusercontent.com/46699116/73037756-110c5180-3e05-11ea-91cb-0c49ff341ce5.png)
