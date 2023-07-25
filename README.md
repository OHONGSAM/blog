# Django-Blog-Project

- Django Blog 제작을 위한 개인프로젝트 repository 입니다

## 1. 프로젝트 목표

- Django를 기반으로 기본적인 기능을 수행하는 블로그를 제작하고 AWS Lightsail을 통해 배포한다.

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

#### - 기술 스택

- <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">

- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

- <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

- <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">

- <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">

- <img src="https://img.shields.io/badge/BootStrap-7952B3?style=for-the-badge&logo=BootStrap&logoColor=white">

#### - 서비스 배포 환경

- <img src="https://img.shields.io/badge/AWS LightSail-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">

### 2.2 배포 URL

- ~~http://13.209.37.52:8000/~~

## 3. 프로젝트 구조와 개발 일정

### 3.1 ERD model

<img width="1434" alt="image" src="https://github.com/vBORIv/Django-Blog-Project/assets/89283288/f905fe08-e11b-467f-abac-7342ee767d4b">

### 3.2 폴더 구조

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

### 3.3 개발 일정

- 2023.07.17 ~ 2023.07.31

## 4. 페이지 화면

### 4.1 Blog

| 메인 페이지                                                                                                          | 글목록                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/607a1394-b396-4700-96d8-de33447a08d1"> | <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/36d53fce-88bd-4825-b613-427ec8355cf6"> |

### 4.2 User 계정

| 회원가입 페이지                                                                                                 | 로그인 페이지                                                                                           |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ![register](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/30ecfdcf-12aa-4e0a-bac7-2c38a0349365) | ![login](https://github.com/vBORIv/ORMI_project_2/assets/89283288/e6a12ed6-0682-4e0e-9503-053cafc71af6) |

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

  | 로그인                                                                                                        | 로그아웃                                                                                                         |
  | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
  | ![loging](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/cd92d699-ea3b-4de7-b953-b254616e39e5) | ![logouting](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/a5889b85-305e-4951-87b6-63d97d0080dd) |

  네비게이션 바는 base.html에서 출력하며, 페이지 인덱싱과 함께 로그인, 로그아웃, 회원가입 버튼을 출력한다. 로그인되어있는 경우에는 로그인된 user의 프로필 사진과 함께 id와 로그아웃 버튼이 출력된다. 프로필 이미지가 없는 유저는 서버에 업로드되어 있는 no_profile.png가 출력된다. 로그인되어있지 않은 경우에는 로그인과 회원가입 버튼을 출력한다.

- 유저 프로필

  | 프로필 수정                                                                                                       | 비밀번호 변경                                                                                                                 |
  | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
  | ![프로필](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/b92e9987-17f4-40f1-94dc-b4ba360d41c7) | ![비밀번호변경](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/629a460f-04fb-4551-aed0-80d9619e2362) |

  네이게이션 바에 출력되는 유저 id를 클릭하여 유저 프로필 페이지로 이동할 수 있다. 유저 프로필 페이지에서는 유저 ID, 프로필 사진을 수정할 수 있다. 비밀번호 변경 페이지는 유저 프로필 페이지로부터 접근할 수 있으며, Django에서 제공하는 `PasswordChangeView`를 이용하여 구현하였다. `(updated at 07.25)`

- 게시글

  | 글작성                                                                                                                         | 글수정                                                                                                                        |
  | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
  | <img width="" alt="write" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/1331a9c8-11ca-4086-886a-3f0fa0fae1a9"> | <img width="" alt="edit" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/2766dbbc-f700-4a21-bf68-e32a3472fa99"> |

  글(post) object는 제목, 내용, 썸네일, 카테고리, 작성일, 수정일을 가지고 있다. 글 작성 시 제목, 내용, 썸네일, 카테고리를 입력할 수 있다. ~~이때 썸네일에 올린 사진은 해당 게시글이 메인 페이지에 뜨게 될 경우 출력된다. 필수 항목은 아니고 썸네일이 없을 경우 서버에 있는 no_thumbnail 이미지가 출력된다.~~ 메인 페이지에 출력되는 썸네일 사진은 글 내용 중 첫번째 사진으로, 정규표현식을 통해 이미지 마크다운 문법(`![name](link)`)을 찾도록 구현하였다.`(updated at 07.25)` 카테고리는 HTML/CSS, Django, Python, 고양이가 있으며, select 태그를 통해 하나를 입력받는다.
  로그인하지 않은 상태에서는 글 작성, 수정, 삭제 버튼이 출력되지 않으며, view에서 LoginRequiredMixin을 상속받아 URL을 통한 접근도 제한된다. 로그인을 한 경우에는 본인이 작성한 게시글에만 글 수정과 삭제 버튼이 출력된다.

- 카테고리 별 목록

  | HTML/CSS                                                                                                                           | Python                                                                                                                             |
  | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/18392fc2-9b1f-4487-bffd-314077d161ae"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/5475bac9-f737-45cc-936d-ab18b191d476"> |

  | Django                                                                                                                             | 고양이                                                                                                                             |
  | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/db531b0c-bbc5-41f2-b430-41f501b10c2d"> | <img width="1000" alt="image" src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/7a7009de-c985-443f-82ae-0f2c1417cabe"> |

  카테고리는 URL에 `<path:category>`를 통해 카테고리 이름을 입력 받아서 해당 페이지로 이동한다. `<str:>`을 사용할 경우 'HTML/CSS'의 슬래쉬를 인식하여 reverse 에러가 발생하기에 `<path:>`를 사용하였다.

- 댓글

  | 비회원                                                                                                                                  | 회원                                                                                                                                   |
  | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
  | <img width="1000" alt="image" src="https://github.com/vBORIv/Django-Blog-Project/assets/89283288/c202cd1e-8df1-43eb-860a-f3d5323ca14f"> | <img width="650" alt="image" src="https://github.com/vBORIv/Django-Blog-Project/assets/89283288/69c0b9ae-65b0-499c-97b8-2f96f4dbfcf6"> |

  로그인하지 않은 경우 댓글을 작성 또는 삭제하지 못한다. 댓글 작성 form이 화면에 출력되지 않을 뿐만 아니라 CommentWrite view에 LoginRequiredMixin을 상속받아 URL을 통한 접근도 제한된다. 로그인한 경우에는 본인이 작성한 댓글만 삭제할 수 있다.

  유저가 프로필에 등록한 프로필 사진이 댓글 목록 옆에 출력되며, 프로필 사진이 없을 경우 서버에 미리 저장된 no_profile.png가 출력된다.`(updated at 07.25)`

- 조회수 및 추천수

  | 조회수                                                                                                               |
  | -------------------------------------------------------------------------------------------------------------------- |
  | <img width=1000 src="https://github.com/vBORIv/ORMI_project_2/assets/89283288/2f66d4db-107a-497f-bbda-4645956ab035"> |

  | 추천                                                                                                        | 추천 취소                                                                                                       |
  | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
  | ![추천](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/6451cb03-d090-4713-8fba-b2656d82a143) | ![추천취소](https://github.com/vBORIv/Django-Blog-Project/assets/89283288/b973533b-d463-41b1-8ced-e5de0ba1a45b) |

  추천 버튼과 함께 받은 추천수가 표시된다. 각 게시글에는 최대 한 번의 추천을 누를 수 있으며, 이미 추천을 누른 게시글에는 추천 버튼의 배경이 채워져서 표시된다. 이미 추천을 누른 게시글의 추천 버튼을 다시 눌러 추천을 취소할 수 있다. `(updated at 07.25)`

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

  ```javascript
  // post_write.html
  const editor = new toastui.Editor({
    el: document.querySelector("#editor"),
    initialEditType: "markdown",
    previewStyle: "vertical",
    height: "300px",
    hooks: {
      addImageBlobHook: function (blob, callback) {
        var formData = new FormData();
        formData.append("image", blob);
        var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        var headers = { "X-CSRFToken": csrftoken };
        fetch("upload-image/", {
          method: "POST",
          body: formData,
          headers: headers,
        })
          .then((response) => response.json())
          .then((result) => {
            var imageUrl = result.image_url;
            callback(imageUrl, "alt text");
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      },
    },
  });
  ```

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

- 썸네일 이미지 `(updated at 07.25)`

  글 작성 시에 추가로 썸네일 이미지를 업로드하지 않고 내용에만 추가하더라도 메인 페이지에 출력될 수 있도록 수정하였다. 글을 작성하고 저장하면, 글 내용에서 `![name](link)` 형식의 이미지 마크다운 문법을 정규표현식으로 찾는 함수를 views.py에 구현하였다. 글 작성 view에서는 앞의 함수를 호출하여 이미지 링크를 추출하고 이를 post.thumbnail_url에 저장한다.

  ```python
  ## views.py
  import re

  def find_img_link(content):
      pattern = r"!\[([^]]+)\]\(([^)]+)\)"
      match = re.search(pattern, content)
      if match:
          name, link = match.groups()
          return name, link
      return None, None


  class PostWrite(LoginRequiredMixin, View):

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            name, link = find_img_link(str(form))
            post = form.save(commit=False)
            post.writer = request.user
            post.thumbnail_url = link
            post.content = request.POST["content"]
            post.save()
            return redirect("blog:list")
        return redirect("blog:list")
  ```

- 중복 추천수 처리 `(updated at 07.25)`

  같은 유저가 중복해서 추천수를 올릴 수 있는 문제를 `Post`와 `User`를 foreign key로 가지는 `Like` model을 추가하여 해결하였다. 추천 버튼을 눌렀을 때, 이미 해당 user와 post를 foreign key로 가지는 Like object가 존재할 경우에는 해당 object를 삭제하여 추천 취소 기능을 구현하였다. 글 디테일 화면을 출력할 때, 로그인되지 않은 유저는 ID 필드를 가지지 않기 때문에 `Like.objects.filter(post=post, user=request.user)`의 DB 호출 과정에서 오류가 발생했다. 따라서 로그인되지 않은 경우에는 무조건 추천을 누르지 않은 상태로 표시되도록 구현하였다.

  ```python
  ## models.py

  class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


  ## views.py

  class PostLike(View):
      def post(self, request, post_id):
          post = get_object_or_404(Post, pk=post_id)

          like = Like.objects.filter(post=post, user=request.user)
          if like:
              like.delete()
          else:
              new_like = Like.objects.create(post=post, user=request.user)
              new_like.save()

          post.likes = Like.objects.filter(post=post).count()
          post.save()
          return redirect("blog:detail", post_id)


  class PostDetail(View):
      def get(self, request, post_id):
          post = get_object_or_404(Post, pk=post_id)
          if request.user.is_authenticated:
              like_chk = True if Like.objects.filter(post=post, user=request.user) else False
              context = {
                  "post": post,
                  "comment_form": CommentForm,
                  "like": like_chk,
              }
          else:
              context = {
                  "post": post,
                  "comment_form": CommentForm,
                  "like": False,
              }
          return render(request, "blog/post_detail.html", context)
  ```

  ```django
  <!-- post_detail.html -->

  <form action="{% url 'blog:like' post_id=post.pk %}" method="post" >
      {% csrf_token %}
      {% if like %}
      <input type="submit" class="btn btn-danger" value="♥︎ {{ post.likes }}" />
      {% else %}
      <input type="submit" class="btn btn-outline-danger" value="♡ {{ post.likes }}" />
      {% endif %}
  </form>
  ```

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

다음은 현재 작동중인 코드에서 특정 상황에 발생하지만 아직 해결하지 못한 오류들이다.

- Toast UI Editor

  Markdown 문법 중 code block 사용 시 조회 및 수정에서 TUI가 인식되지 않는 오류

- 글 목록 UI

  글 목록의 테이블 헤더가 특정 상황에서 여러 줄로 출력되는 현상

### 6.2 코드 개선

다음은 현재 기능은 제대로 동작하지만 구현하고 돌아보는 과정에서 찜찜함이 느껴졌던 부분이다. 프로젝트를 급하게 진행하면서 다른 기능들이 우선 작동이라도 하도록 만들기 위해 지나쳤던 부분이다. 실제 베포를 진행하여 서버로 많은 쿼리가 몰리게 될 경우 충분히 치명적인 문제를 발생시킬 수 있는 부분으로 보인다.

- 글 목록 페이지 기능 중복

  전체글, 인기글, 카테고리 별 페이지가 모두 글 목록 출력, sort 기준에 따른 목록 정렬 기능을 가지지만 빠른 기능 구현을 위해 각각 다른 view class를 생성했다. URL pattern을 통해 분류하여 하나의 view class로 만듦으로써 코드의 중복을 줄일 수 있다.

- 중복된 기능의 DB 쿼리

  제목/내용을 기준으로 검색하게 되면 키워드가 제목 또는 내용에 포함된 게시글을 DB로부터 새로 찾아온다. 그러나 글목록 화면에서 검색하는 경우에는 이미 글 목록을 DB로부터 불러온 상태이다. 따라서 댓글 내용에서 검색을 하는게 아닌 이상, 다시 DB에서 검색을 하는 것은 불필요하다.

  글 목록을 정렬하는 기능은 GET request를 통해 view에 sort 변수를 전달하고 orderby(sort)로 DB로부터 새롭게 목록을 불러온다. 앞에서 말한 검색의 경우와 같은 상황으로, 이미 글 목록을 불러와 출력한 상황에서 다시 DB에 쿼리를 보내는 것은 불필요하다. 따라서 dictsort와 같은 Django template 문법을 활용하여, 화면에 출력한 글 목록을 정렬하는 방식으로의 개선이 필요하다.

### 6.3 추가 기능 구현

다음은 이번 프로젝트를 진행하면서 머리 속으로 틈틈이 구상하던 기능들이다. 구현하는 방법은 자명하지만 시간이 부족하여 완성하지 못한 기능들도 있고, 구현하는 방법을 아직 고민하고 있던 기능들도 있다. 대댓글, 유저 프로필과 같은 부분은 블로그 페이지에 필수적인 기능이기 때문에 프로젝트 기간 이후에도 구현해볼 것이다.

- 댓글

  대댓글 기능, 댓글 좋아요 및 신고 기능을 추가할 수 있다. 대댓글 기능의 경우 parent comment와 child comment를 속성으로 가지는 model을 통해 구현한다면 depth 2 이상의 대댓글 기능을 구현할 수 있을 것이다.

- 유저

  ~~프로필 페이지를 만들고 프로필 사진을 업로드하거나 비밃번호 변경과 같은 기능을 추가할 수 있다. 유저의 프로필 사진은 작성한 댓글에 연결하여 댓글 작성자의 ID와 함께 출력할 수 있다.~~ (구현 완료) `(updated at 07.25)`

  유저 프로필 페이지에서 회원 탈퇴 기능을 추가할 수 있다. 이때 해당 user object를 DB에서 삭제하는 것이 아니라 Django에서 제공하는 is_active 속성을 false로 변경하여 저장할 수 있다.

  댓글에 유저 ID와 함께 출력되는 프로필 사진을 눌러 해당 유저의 프로필을 볼 수 있도록 구현할 수 있다.

- UI

  ~~현재 로그인, 회원가입 화면에는 Django의 form을 그대로 출력하고 있다. 심지어는 중앙 정렬도 하지 않은 상태이다.~~ (구현 완료) `(updated at 07.25)`

- 에러 페이지

  백엔드에서 404 ERROR와 form ERROR를 발생시키는 경우는 views.py에서 고려하였다. 하지만 이를 프론트엔드에 출력하는 화면을 만들지 못했다. 404 ERROR가 발생했을 때는 없는 게시물임을 명시하고 이전 페이지나 메인 페이지로 이동할 수 있는 버튼이 필요하다. form ERROR는 어떤 부분에서 어떤 에러가 발생했는데 화면에 명시하고, 에러가 발생하지 않도록 맞춰야하는 기준을 출력해야 한다.

- 글 목록 오름차순 정렬

  현재는 작성일, 조회수, 추천수를 기준으로 내림차순 정렬만 가능하다. 따라서 정렬 링크를 다시 눌렀을 때 오름차순으로 정렬되는 기능이 추가적으로 구현될 수 있다.

- 조회 & 추천 중복 카운트

  게시글 추천 기능의 초기 구현 단계에서는 추천 후 해당 게시글의 상세 페이지로 redirect될 때 조회수가 1 증가하는 문제가 발생하였다. 이는 추천 버튼을 눌렀을 때 조회수를 1 감소시키는 방법으로 해결하였다.

  ~~같은 유저가 같은 게시글을 중복하여 조회하거나 추천했을 때 중복 카운트되는 문제는 아직 해결하지 못하였다. 메인 페이지 노출이 추천수만을 기반으로 결정되기 때문에 조회수의 중복 카운트는 크게 문제되지 않을 수 있다. 그러나 추천수가 중복되어 카운트되는 문제는 실제 베포를 위해서는 반드시 해결해야할 부분이다.~~ (구현 완료) `(updated at 07.25)`

- 메인 페이지 위젯

  메인 페이지 오른쪽에 위젯이 존재한다. 검색 위젯은 게시글 검색 기능과 연결하여 검색 페이지로 이동할 수 있도록 만들 수 있다. 다른 위젯에는 한 주 동안 게시글이나 댓글을 많이 받은 유저들의 목록을 출력할 수 있다. 이 기능을 구현하기 위해서는 comment object를 writer를 기준으로 group by 하여 user object와 join하는 과정이 필요할 것이다. 또한 게시글 작성 수, 댓글 작성 수, 받은 추천 수를 모두 고려하는 특정 알고리즘으로 등수를 계산할 수도 있을 것이다.

- 블로그 현재 접속자 수 계산

  Django의 session 기능을 활용하여 저장되어 있는 session의 수로 현재 접속자 수를 대략적으로 계산할 수 있을 것이다. 그러나 browser cookie가 삭제되더라도 session을 유지되기 때문에 session 갱신 주기의 길이에 반비례하여 현재 접속자 수의 정확도가 낮아질 것이다. Django의 cache 기능을 사용하거나, 웹 서버의 기능을 이용하는 것과 같은 보다 정교한 방법이 있을 것이다.

## 7. 개발 과정에서 느낀점

프로젝트를 진행하면서 가장 체감이 컸던 부분은 바로 시간이었다. Django를 이용한 프로젝트가 처음이었기에 이런저런 기능을 활용하기가 익숙치 않아서 진행이 생각보다 더디었다. Toast UI Editor를 적용하는 것과 같은 Django 외적인 부분에서 시간이 많이 소모되기도 했다. 특히 프로젝트 기간 마지막 목요일에 readme 파일을 작성하는 과정에서 GIF 파일이 제대로 동작하기 않아서 크게 애를 먹었다. (원인은 맥에서 녹화한 동영상의 크기가 너무 큰 탓이었다) 그러나 이는 프로젝트를 시작하면서도 예상 가능한 어려움이었다. 무엇보다 가장 아쉽게 느껴지는 부분은 특정 기능을 구현하는 데에 어느 정도 시간이 걸릴 지조차 예측하기 어려웠던 점이었다. 간단하게 구현할 수 있을 거라 생각했던 부분에서 예상치 못한 난관에 봉착하는 경우가 더러 있었다. 때문에 적어도 main 페이지의 widget에 데이터를 연결하고 회원가입 페이지와 같은 여러 UI까지는 손볼 수 있을 줄 알았던 나의 예상은 빗나가버렸다.

좋은 개발자는 얼마나 높은 퀄리티의 코드를 짜는지가 아니라 항상 일정 수준 이상의 코드를 짜는 것이 중요하다고 한다. 개발자에게 중요한 건 시간이다. 절대적인 코딩 속도를 높이는 것은 중요하며, 이는 코딩에 쏟은 시간이 해결해줄 것이다. 하지만 추가적으로 본인이 코드를 완성하는데 얼마나 걸릴지 정확하게 예측할 수 있는 능력도 매우 중요하다고 생각한다. 이는 또한 코딩에 쏟은 시간이 해결해줄 것이다. 따라서 코딩에 시간을 쏟아야 한다.
