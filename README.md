# resume

The goal of this project is to provide a simple application to build a resume and output it in various formats such as PDF, DOCX, JSON, etc.

This uses docker-compose to facilitate the development environment.

First run requires running migrations while the docker-compose containers are running.


`docker-compose run web python3 manage.py makemigrations viewer`  
`docker-compose run web python3 manage.py migrate`
`docker-compose up`

Landing Page:

![image](https://user-images.githubusercontent.com/46699116/73309396-fbb56f80-41d6-11ea-9138-2aebfb565a0d.png)

HTML:

![image](https://user-images.githubusercontent.com/46699116/73037717-ea4e1b00-3e04-11ea-8dd1-317a8c0b7392.png)

JSON:

![image](https://user-images.githubusercontent.com/46699116/73037756-110c5180-3e05-11ea-91cb-0c49ff341ce5.png)

DOCX:
![image](https://user-images.githubusercontent.com/46699116/73890946-f637d500-4827-11ea-8883-9f0f2e263743.png)
