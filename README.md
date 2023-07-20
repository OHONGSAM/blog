# ORMI_Project_2

- Django Blog 제작 개인프로젝트 repo 입니다

## 1. 목표와 기능

### 1.1 목표

- ...

### 1.2 기능

- ...

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

- 개발 환경

  - Django
  - Python
  - JavaScript

- 서비스 배포 환경
  - AWS LightSail

### 2.2 배포 URL

- http://13.209.37.52:8000/

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조

```
Project_2
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── thumbnails
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   ├── est.jpg
│   ├── thumbnails
│   └── uploads
├── requirements.txt
├── static
├── templates
│   ├── 404.html
│   ├── base.html
│   └── index.html
├── user
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```

### 3.2 개발 일정

#### 개발 일정

2023.07.17 ~ 2023.07.21

#### 기술 스택

- Django
- Python
- JavaScript
- BootStrap CSS

## 4. 페이지 화면

### 4.1 블로그 화면

메인 페이지
![main](https://github.com/vBORIv/ORMI_project_2/assets/89283288/b2b63741-cce3-468e-8916-8478968a84a0)

글 전체 목록
![blog_list](https://github.com/vBORIv/ORMI_project_2/assets/89283288/495c4197-c53c-4ebb-8e20-5e5c1c1b8025)

### 4.2 유저 관련 화면

회원가입 페이지
![register](https://github.com/vBORIv/ORMI_project_2/assets/89283288/b97bbadd-1944-4582-be90-1c2d07562e3e)

로그인 페이지
![login](https://github.com/vBORIv/ORMI_project_2/assets/89283288/e6a12ed6-0682-4e0e-9503-053cafc71af6)

## 5. 기능

### 5.1 URL 리스트

| URL                                             | 기능                 |
| ----------------------------------------------- | -------------------- |
| '/'                                             | 메인페이지           |
| '/user/register'                                | 회원가입             |
| '/user/login'                                   | 로그인               |
| '/user/logout'                                  | 로그아웃             |
| '/blog/'                                        | 전체글 목록          |
| '/blog/write'                                   | 게시글 작성          |
| '/blog/write/upload-image'                      | 게시글 이미지 업로드 |
| '/blog/detail/\<int:post_id>'                   | 게시글 상세          |
| '/blog/detail/\<int:post_id>/edit'              | 게시글 수정          |
| '/blog/detail/\<int:post_id>/edit/image-upload' | 게시글 이미지 수정   |
| '/blog/detail/\<int:post_id>/delete'            | 게시글 삭제          |
| '/blog/detail/\<int:post_id>/comment/write'     | 댓글 작성            |
| '/blog/detail/\<int:post_id>/comment/delete'    | 댓글 삭제            |
| '/blog/detail/\<int:post_id>/like'              | 게시글 추천          |
| '/blog/search'                                  | 검색                 |
| '/blog/hot'                                     | 인기글 목록          |
| '/blog/\<path:category>'                        | 카테고리별 글목록    |

### 5.2 주요 기능

- 글작성
- 글수정
-

### 5.2 세부 기능

## 6. 향후 개선 사항

## 7. 개발 과정에서 느낀점
