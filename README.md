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

### 4.1 Blog

| 메인 페이지                                                                                            | 전체글 목록                                                                                                 |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| ![main](https://github.com/vBORIv/ORMI_project_2/assets/89283288/e79dc3ff-2cbf-467a-b538-d79808a40af8) | ![post-list](https://github.com/vBORIv/ORMI_project_2/assets/89283288/495c4197-c53c-4ebb-8e20-5e5c1c1b8025) |

### 4.2 User 계정

| 회원가입 페이지                                                                                            | 로그인 페이지                                                                                           |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ![register](https://github.com/vBORIv/ORMI_project_2/assets/89283288/b97bbadd-1944-4582-be90-1c2d07562e3e) | ![login](https://github.com/vBORIv/ORMI_project_2/assets/89283288/e6a12ed6-0682-4e0e-9503-053cafc71af6) |

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

- 로그인 로그아웃

| 로그인                                                                                                     | 로그아웃                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ![logining](https://github.com/vBORIv/ORMI_project_2/assets/89283288/3e261e11-268d-49d9-ba4a-09792d6ab61d) | ![logouting](https://github.com/vBORIv/ORMI_project_2/assets/89283288/dba06dc4-da44-4ff1-b5cf-30a4e6b28932) |

- 게시글

| 글 작성                                                                                                                            | 글 수정                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/ebc093d4-1c39-4c4d-802b-d5d01c2ab350"> | <img width="900" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/032991b0-f3ed-4501-9efe-268b21bddecb"> |

- 카테고리 별 목록

| HTML/CSS                                                                                                                           | Python                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/132e3894-66ab-41c2-a558-2ecbd74c84e2"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/70ec1568-a02f-460e-aa33-5c184f7a541c"> |

| Django                                                                                                                             | 고양이                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/9de8e05a-4ec9-4f86-b249-baf68daec20b"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/0ada0e45-f03c-4fc7-bdeb-f0b68843f825"> |

- 댓글

| 비회원                                                                                                                             | 회원                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/02eb61a5-5332-4d65-a588-b7f6df3cba2b"> | <img width="680" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/549e40cd-7a32-4a83-abae-735224ccec66"> |

- 게시글 조회수
  <img width="" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/8e5e12c8-be84-4c53-85e9-fc94f77f07bd">

- 게시글 추천수

- 검색
  <img width="" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/bb1b9e71-8ac1-4599-8283-1f7fa0e11983">

- 글 정렬

| 작성일                                                                                                                         | 조회수                                                                                                                         | 추천수                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| <img width="" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/f8f711db-dc86-41dc-98eb-f0bb901ccd4a"> | <img width="" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/fd6650a6-7f5b-41f4-91a6-0b98cee52541"> | <img width="" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/6a5a3e76-fa4f-42a8-804e-ad4a2bc7c45d"> |

### 5.2 세부 기능

- Toast UI Editor (글 중간 이미지 업로드, markdown)
  <img width="1087" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/8655056f-7f1e-4fad-bd4a-ea373a79bf7a">

  ```
    Toast UI Editor를 사용하여 markdown 문법을 사용하여 글을 작성할 수 있고, 글 중간에 이미지를 삽입할 수 있다. 이때 삽입된 이미지는 base64 형식으로 인코딩하지 않고, 서버의 '/media/uploads/'에 업로드하여 path로 접근한다.
  ```

- 메인 페이지에 게시될 글 추출
  <img width="1179" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/7c0e5d32-4814-47c0-826f-a14214b64416">

  ```
    메인페이지에는 추천수가 많은 순서대로 최대 5개의 글이 출력된다. 이때 보여지는 썸네일 이미지는 글 작성 시 업로드할 수 있으며, 서버의 '/media/thumbnails/'에 저장된다. 썸네일이 없는 게시글은 '/media/thumbnails/no_img.jpg' 파일로 대체된다.
    게시글 카드에는 작성일, 카테고리, 제목, 내용이 있다. 내용은 게시글의 앞부분 내용을 일부 보여주고 '...'으로 생략한다.
  ```

- 반응형 페이지

| 전체 화면                                                                                                                         | 좁은 화면                                                                                                                         | 좁은화면 네비게이션                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="700" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/88f645ca-1d28-4de8-bb57-672e43c4a7b4"> | <img width="450" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/428d213b-880d-4749-b815-a45be4c89268"> | <img width="450" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/df995499-935b-4516-8b3a-c398dcdca472"> |

- Pagenation

| 첫페이지                                                                                                                           | 중간페이지                                                                                                                         | 마지막페이지                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1175" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/402d0ebf-2979-434e-9445-ddbc94aea63e"> | <img width="1178" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/5abeacf1-35e5-4252-a138-c7d66f20e5f0"> | <img width="1175" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/b145d5f7-cfc7-46f3-9ab4-6c27485de6de"> |

## 6. 향후 개선 사항

### 6.1 코드 에러

- Toast UI Editor
  ```
  Markdown 문법 중 code block 사용 시 조회 및 수정에서 TUI가 인식되지 않는 오류
  ```

### 6.2 코드 개선

- 카테고리 별 페이지, 전체글, 인기글 페이지가 거의 같은 기능인데 각각 다른 view 클래스로 구현됨

- search 시 검색 키워드에 일치하는 post object를 db에서 검색함
  -> db 호출이 많아져 오래 걸릴 수 있음
  -> 현재 화면에 출력하고 있는 목록에서 찾으면 DB 호출수 낮출 수 있음

- 정렬 시 get request로 정렬 방법을 읽어서 order by로 DB 호출함
  -> DB 호출이 많아져 오래 걸릴 수 있음 & 검색 결과를 정렬하지 못함
  -> 현재 화면에 출력하고 있는 목록을 이용해서 정렬하는 방법 필요 (dictsort)

-

### 6.3 추가 기능 구현

- 글 목록을 조건에 따라 오름차순으로도 가능하도록

- 메인 페이지 위젯

  - 검색 시 검색 페이지로 연결
  - 댓글을 많이 작성한 유저 수

- Django의 session 수를 활용하여 현재 접속자 수를 대략적으로 계산

- 댓글

  - 대댓글 기능
  - 댓글 좋아요 및 신고 기능

- 유저

  - 개인정보 수정 (비밀번호, 프로필 사진 ,,)
  - 프로필 페이지

- UI
  - 로그인, 회원가입 화면
  -

## 7. 개발 과정에서 느낀점
