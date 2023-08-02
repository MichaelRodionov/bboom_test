# Test task for BBoom company
## Tech stack:
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>     
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>  
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>

## This application consists of 2 main modules:   
- API interface
- UI interface   
### API features:
- Registration and authorization with JWT;
- Get list of Users;
- Create Post;
- Get a list of Posts by a specific user;
- Delete Post.
### UI features:
- Authorization with session (using django authentication form);
- Get list of Users (Click on the user and the page with his Posts will open);
- Create Post (using django form);
- Delete Post.

### Project structure
- `bboom_test/` : package with django settings
- `posts/` : posts django app
- `users/` : users django app
- `tests/` : testing application package
- `ui/` : ui django app
- `pyproject.toml` : dependencies file
- `Dockerfile` : container configuration
- `docker-compose.yaml` : docker-compose file
- `pytest.ini` : pytest configuration
- `manage.py` : main django file

### Local start
1) Clone repository
``` python
git clone https://github.com/MichaelRodionov/bboom_test.git
```
2) Create your own repository   
3) Add remote to your GitHub repository by repository URL   
4) Push code to your repository
``` python
git add .  # add all files to Git
git commit -m 'add project'  # initial commit
git push  # push to repository
```
4) Create virtual environment   
5) Create local `.env` file with the next data:  
``` python
SECRET_KEY='your django key'
DATABASE_URL=postgres://postgres:postgres@db/todo_list
DEBUG=False
```
6) Start docker
``` python
docker-compose up --build
```
### API requests are available on address http://127.0.0.1:8000
### UI requests are available on address http://127.0.0.1:8080