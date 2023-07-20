# [ORMI_Project] Django-Blog

- Django Blog 제작 개인프로젝트 repo 입니다

## 1. 프로젝트 목표

- Django를 기반으로 기본적인 기능을 수행하는 블로그를 제작하고 AWS Lightsail을 통해 배포한다.

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

- 개발 환경

  - Django
  - Python
  - JavaScript

- 서비스 배포 환경
  - AWS Lightsail (Ubuntu)

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

#### - 개발 일정

- 2023.07.17 ~ 2023.07.20

#### - 기술 스택

- Django
- Python
- JavaScript
- HTML
- BootStrap CSS

## 4. 페이지 화면

### 4.1 Blog

| 메인 페이지                                                                                                          | 전체글 목록                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/607a1394-b396-4700-96d8-de33447a08d1"> | <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/36d53fce-88bd-4825-b613-427ec8355cf6"> |

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

  | 로그인                                                                                                   | 로그아웃                                                                                                    |
  | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
  | ![loging](https://github.com/vBORIv/ORMI_project_2/assets/89283288/0baddd44-71df-45af-898c-30fca4be0bee) | ![logouting](https://github.com/vBORIv/ORMI_project_2/assets/89283288/57164bc5-d0a3-4c3f-b6f1-7308a3d95761) |

  Navigation Bar는 base.html에서 출력하며, 페이지 인덱싱과 함께 로그인, 로그아웃, 회원가입 버튼을 출력한다. 로그인되어있는 경우에는 로그인된 user id와 로그아웃 버튼이 출력된다. 로그인되어있지 않은 경우에는 로그인과 회원가입 버튼을 출력한다.

- 게시글

  | 글작성                                                                                                                         | 글수정                                                                                                                        |
  | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
  | <img width="" alt="write" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/1331a9c8-11ca-4086-886a-3f0fa0fae1a9"> | <img width="" alt="edit" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/2766dbbc-f700-4a21-bf68-e32a3472fa99"> |

  글(post) object는 제목, 내용, 썸네일, 카테고리, 작성일, 수정일을 가지고 있다. 글 작성 시 제목, 내용, 썸네일, 카테고리를 입력할 수 있다. 이때 썸네일에 올린 사진은 해당 게시글이 메인 페이지에 뜨게 될 경우 출력된다. 필수 항목은 아니고 썸네일이 없을 경우 서버에 있는 no_thumbnail 이미지가 출력된다. 카테고리는 HTML/CSS, Django, Python, 고양이가 있으며, select 태그를 통해 하나를 입력받는다.
  로그인하지 않은 상태에서는 글 작성, 수정, 삭제 버튼이 출력되지 않으며, view에서 LoginRequiredMixin을 상속받아 URL을 통한 접근도 제한된다. 로그인을 한 경우에는 본인이 작성한 게시글에만 글 수정과 삭제 버튼이 출력된다.

- 카테고리 별 목록

  | HTML/CSS                                                                                                                           | Python                                                                                                                             |
  | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/18392fc2-9b1f-4487-bffd-314077d161ae"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/5475bac9-f737-45cc-936d-ab18b191d476"> |

  | Django                                                                                                                             | 고양이                                                                                                                             |
  | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/db531b0c-bbc5-41f2-b430-41f501b10c2d"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/7a7009de-c985-443f-82ae-0f2c1417cabe"> |

  카테고리는 URL에 \<path:category>를 통해 카테고리 이름을 입력 받아서 해당 페이지로 이동한다. \<str:>을 사용할 경우 'HTML/CSS'의 슬래쉬를 인식하여 reverse 에러가 발생하기에 \<path:>를 사용하였다.

- 댓글

  | 비회원                                                                                                                             | 회원                                                                                                                              |
  | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/02eb61a5-5332-4d65-a588-b7f6df3cba2b"> | <img width="680" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/549e40cd-7a32-4a83-abae-735224ccec66"> |

  로그인하지 않은 경우 댓글을 작성 또는 삭제하지 못한다. 댓글 작성 form이 화면에 출력되지 않을 뿐만 아니라 CommentWrite view에 LoginRequiredMixin을 상속받아 URL을 통한 접근도 제한된다. 로그인한 경우에는 본인이 작성한 댓글만 삭제할 수 있다.

- 조회수 및 추천수 카운트

  | 조회수                                                                                                               | 추천수                                                                                                               |
  | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
  | <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/2f66d4db-107a-497f-bbda-4645956ab035"> | <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/a74105b1-f060-49d5-b7e1-d6e4cf51fc3e"> |

- 검색

  <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/200433b3-5978-446f-8c68-bca36667f565">

  제목/내용, 댓글, 카테고리를 기준으로 검색할 수 있다. 검색된 결과로 출력되는 게시글들은 작성된 시간 기준으로 내림차순으로 정렬된다.

- 글 정렬

  | 작성일                                                                                                                  | 조회수                                                                                                               | 추천수                                                                                                                |
  | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
  | ![정렬_작성일](https://github.com/vBORIv/ORMI_project_2/assets/89283288/b6f6ffaf-c233-4b58-a400-c83f8e2e5f2e) | ![정렬_조회수](https://github.com/vBORIv/ORMI_project_2/assets/89283288/126a379b-4ba1-46df-9717-71780c6e6dae) | ![정렬_추천수](https://github.com/vBORIv/ORMI_project_2/assets/89283288/2bd6c0b7-6192-48e0-aae9-4909d67cb752) |

  게시글 목록은 해당하는 column의 table header를 클릭하여 작성일, 조회수, 추천수를 기준 내림차순으로 정렬할 수 있다. 기본 정렬방식은 작성일이 기준이다. 정렬 기준을 선택하면 GET request로 URL 뒷부분에 sort 변수를 담아 view로 전달하고, context에 담아 페이지를 다시 호출한다.

  ```python
  ## URL : 'blog/?sort=views'
  sort = request.GET.get("sort")
  context = {
            "posts": page,
            "sort": sort,
  }
  ```

  이를 다시 template에서 dictsortreversed를 이용하여 정렬한다.

  ```django
  {% for post in posts|dictsortreversed:sort %}
    {{ post.content }}
  {% endfor %}
  ```

### 5.2 세부 기능

- Toast UI Editor (글 중간 이미지 업로드, markdown)
  <img width="1087" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/8655056f-7f1e-4fad-bd4a-ea373a79bf7a">

  Toast UI Editor를 적용하여 markdown 문법을 사용하여 글을 작성할 수 있고, 글 중간에 이미지를 삽입할 수 있다. django_tuieditor를 프로젝트 내부에 app으로 설치하여 post의 content를 MarkdownField로 적용해보려고 시도하였으나 끝내 화면에 출력하지 못하고 CDN 방식으로 진행하였다. 'editor'라는 id를 가지는 html element를 새로 생성하여, 작성 제출 버튼이 눌리게 되면 toastui.Editor의 내용이 input 태그로 들어가고, POST.request에 담겨 view에 전달된다. 이를 views.py에서 post.content에 넣고 저장한다.

  ```html
  <!-- post_write.html -->
  <div id="editor"></div>
  <input type="hidden" name="content" value="value" />
  <script>
    const editor = new toastui.Editor({
      el: document.querySelector("#editor"),
      initialEditType: "markdown",
      previewStyle: "vertical",
      height: "300px",
    });
    const submitBtn = document.getElementById("btn-submit");
    submitBtn.addEventListener("click", function (event) {
      event.preventDefault();
      const content = editor.getMarkdown();
      document.querySelector("input[name='content']").value = content;
      submitBtn.closest("form").submit();
    });
  </script>
  ```

  ```python
  ## views.py
  post.content = request.POST["content"]
  ```

  삽입된 이미지는 base64 형식으로 인코딩하지 않고, 우선 'blog/write/upload-image/'의 URL로 접근하여 서버의 '/media/uploads/'에 업로드한다. 이후 업로드된 path를 markdown 문법에 삽입하여 이미지를 출력한다. Markdown 이미지 삽입 문법을 사용하기 위해 웹 상에서 서버 이미지에 접근할 수 있는 경로가 필요하다. 따라서 파일이 저장된 경로에 접근하기 위해 MEDIA_ROOT와 MEDIA_URL를 새로 작성하고, URL pattern에 추가하였다. 또한 로컬 서버에서 이미지 업로드 작동을 테스트하기 위해 local_path를 "http://127.0.0.1:8000/media"로 선언하였다. 이후 AWS에서 서버 구동을 확인할 때에는 aws_path를 이용하여 접근하도록 변경하였다.

  ```python
  ## views.py
  def upload_image(request, post_id=None):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        filename = image.name
        upload_path = os.path.join(settings.MEDIA_ROOT, "uploads", filename)
        local_path = "http://127.0.0.1:8000/media"
        aws_path = "http://13.209.37.52:8000/media"

        with open(upload_path, "wb") as file:
            for chunk in image.chunks():
                file.write(chunk)

        image_url = local_path + "/uploads/" + filename

        return JsonResponse({"image_url": image_url})

    return JsonResponse({"error": "Invalid request"}, status=400)

  ## settings.py
  MEDIA_ROOT = os.path.join(BASE_DIR, "media")
  MEDIA_URL = "media/"

  ## blog/urls.py
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

- 메인 페이지에 게시될 글 추출
  <img width="1179" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/7c0e5d32-4814-47c0-826f-a14214b64416">

  메인페이지에는 추천수가 많은 순서대로 최대 5개의 글이 출력된다. 이때 보여지는 썸네일 이미지는 글 작성 시 업로드할 수 있으며, 서버의 '/media/thumbnails/'에 저장된다. 썸네일이 없는 게시글은 '/media/thumbnails/no_img.jpg' 파일로 대체된다. 게시글 카드에는 작성일, 카테고리, 제목, 내용이 있다. 내용은 게시글의 앞부분 내용을 일부 보여주고 '...'으로 생략한다. 썸네일 이미지와 Read more 버튼에 해당 글의 링크를 연결하였다. 카테고리 배지에는 해당 카테고리 페이지 링크를 연결하였다.

- 반응형 페이지

  | 전체 화면                                                                                                                         | 좁은 화면                                                                                                                         | 좁은화면 네비게이션                                                                                                               |
  | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="700" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/88f645ca-1d28-4de8-bb57-672e43c4a7b4"> | <img width="450" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/428d213b-880d-4749-b815-a45be4c89268"> | <img width="450" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/df995499-935b-4516-8b3a-c398dcdca472"> |

  | 반응형 페이지                                                                                                  | 반응형 네비게이션                                                                                              |
  | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
  | ![반응형페이지](https://github.com/vBORIv/ORMI_project_2/assets/89283288/bb2533ae-dcd4-4d17-b0b9-2f592b3bf48b) | ![반응형햄버거](https://github.com/vBORIv/ORMI_project_2/assets/89283288/b6a8f227-5580-44a4-afd2-a5f170737c78) |

  반응형 페이지는 Bootstrap CSS를 활용하여 만들었다. 네비게이션 바는 window의 width가 좁아짐에 따라 햄버거 버튼이 생성되고, 토글로 로고를 제외한 버튼들을 선택할 수 있도록 만들었다. 메인 페이지와 글 상세 페이지의 CSS는 [Start Bootstrap](https://startbootstrap.com/template/blog-post)의 템플릿을 이용하였다.

- Pagenation

  | 첫페이지                                                                                                                           | 중간페이지                                                                                                                         | 마지막페이지                                                                                                                       |
  | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1175" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/402d0ebf-2979-434e-9445-ddbc94aea63e"> | <img width="1178" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/5abeacf1-35e5-4252-a138-c7d66f20e5f0"> | <img width="1175" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/b145d5f7-cfc7-46f3-9ab4-6c27485de6de"> |

    <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/c7e002b2-d96a-4e9b-9e4b-24efb5c26295">

  Pagenation은 Django의 paginator 기능을 사용하여 구현하였다.

  ```python
  ## views.py
  # 페이지당 보여줄 포스트 수
  posts_per_page = 6

  # 현재 페이지 번호 가져오기
  page_number = request.GET.get("page", 1)

  # Paginator 객체 생성
  paginator = Paginator(posts_sorted, posts_per_page)

  try:
      # 현재 페이지에 해당하는 포스트 가져오기
      page = paginator.page(page_number)
  except InvalidPage:
      # 유효하지 않은 페이지 번호일 경우 첫 번째 페이지로 이동
      page = paginator.page(1)

  context = {
      "posts": page,
      "sort": sort,
  }
  ```

  template 상에서 이전 page 또는 다음 page가 존재하는 경우에만 해당 버튼이 출력되도록 하였다.

  ```django
  {% if posts.has_other_pages %}
    {% if posts.has_previous %}
    <!-- print previous button -->
    {% endif %}
  {% endif %}
  ```

- 존재하지 않는 게시글 처리

  글 상세 페이지와 수정 페이지는 post의 pk를 이용하여 특정 게시글을 DB로부터 불러오기 때문에 해당 게시글이 존재하지 않으면 오류가 발생할 수 있다. 따라서

  ```python
  post = Post.object.get(pk=post_id)
  ```

  이 아닌

  ```python
  post = get_object_or_404(Post, pk=post_id)
  ```

  를 사용하여 해당 게시글이 DB에 존재하지 않을 경우 404 에러를 발생시키도록 하였다.

## 6. 향후 개선 사항

### 6.1 코드 에러

- Toast UI Editor

  Markdown 문법 중 code block 사용 시 조회 및 수정에서 TUI가 인식되지 않는 오류

-

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

- 조회 및 추천 중복 카운트

- 메인 페이지 위젯

  - 검색 시 검색 페이지로 연결
  - 댓글을 많이 작성한 유저 수

- Django의 session 수를 활용하여 현재 접속자 수를 대략적으로 계산

- 댓글

  - 대댓글 기능
  - 댓글 좋아요 및 신고 기능
  - 댓글 유저 프로필

- 유저

  - 개인정보 수정 (비밀번호, 프로필 사진 ,,)
  - 프로필 페이지

- UI

  - 로그인, 회원가입 화면
  -

- 에러 페이지
  - 404 ERROR
  - form ERROR

## 7. 개발 과정에서 느낀점

프로젝트를 진행하면서 가장 체감이 컸던 부분은 바로 시간이었다. Django를 이용한 프로젝트가 처음이었기에 이런저런 기능을 활용하기가 익숙치 않아서 진행이 생각보다 늦었다. Toast UI Editor를 적용하는 것과 같은 Django 외적인 부분에서 시간이 많이 소모되기도 했다. 특히 마지막 목요일에 진행한 readme 파일을 작성할 때 GIF 파일이 제대로 동작하기 않아서 크게 애를 먹었다. (원인은 맥에서 녹화한 동영상의 크기가 너무 큰 탓이었다) 그러나 이는 프로젝트를 시작하면서도 예상 가능한 어려움이었다. 무엇보다 가장 아쉽게 느껴지는 부분은 내가 어느 정도 시간이 걸릴 지조차 예측하기 어려웠던 점이었다.

때문에 적어도 main 페이지의 widget에 데이터를 연결하고 회원가입 페이지와 같은 여러 UI까지는 손볼 수 있을 줄 알았던 나의 예상은 빗나가버렸다.

좋은 개발자는 얼마나 높은 퀄리티의 코드를 짜는지가 아니라 항상 일정 수준 이상의 코드를 짜는 것이 중요하다고 한다.
개발자에게 중요한 건 시간이다.

절대적인 코딩 속도를 높이는 것은 중요하며, 이는 코딩에 쏟은 시간이 해결해줄 것이다. 하지만 추가적으로 본인이 코드를 완성하는데 얼마나 걸릴지 정확하게 예측할 수 있는 능력도 매우 중요하다고 생각한다. 이는 또한 코딩에 쏟은 시간이 해결해줄 것이다. 따라서 코딩에 시간을 쏟아야 한다.

```

```
