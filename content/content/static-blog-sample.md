Title: GitHub Pages와 travis-ci를 이용한 정적 블로그 구축하기
Date: 2014-02-01
Tags: blog, static site generator
Category: etc
Slug: static-blog-sample
Author: if1live
Summary: GitHub Pages + travis-ci + etc..


내가 GitHub Pages를 사용한지 대략 1년정도 지났다.
그동안 어떻게 설정하면 관리하기 편하지 실험도 몇번 해봤고
테마도 하나 만들어서 사용해봤고
travis-ci와 연동해서 완전 자동화도 끝냈다.
정적블로그로 해볼만한거 어느정도 한거같아서 남들한테 영업좀 해볼겸 정리를 해봤다.

다음을 대상으로 내용을 작성했다.

* 개인 블로그를 정적 블로그로 만드려고 하는 사람
* 자신의 정적 블로그가 2% 부족해보이는 사람
* 블로그의 완전 자동화를 목표로 하는 사람

주의 : 정적블로그의 장점은 이 글에서는 다루지 않는다. [정적 웹사이트 생성기의 유혹][static-site-generator]을 참고


## Double Repository

GitHub Pages는 2가지 상황에서 동작이 다르다.

* 계정(혹은 회사)에 딸린 pages. <username>.github.io 프로젝트의 master 브렌치를 사용한다.
* 프로젝트에 딸린 pages. gh-pages 저장소를 새로 만들어서 사용한다. 글의 목표가 개인 블로그를 만드는것이니까 프로젝트에 딸린 pages에 대해서는 취급하지 않는다.


github pages의 경우 <username>.github.io 에 있는 내용을 그대로 웹에 보여준다. 블로그 내용을 내용을 <username>.github.io 에 집어넣고 자동생성된 html도 <username>.github.io 에 존재하면 저장소가 깨끗하지 않다. 데이터도 섞여있고 커밋로그도 섞여있다.

그래서 저장소를 2개로 분리하는게 좋다.

* 실제 블로그 내용이 있는 저장소. 앞으로 **content repo** 라고 부른다.
* 생성된 html만 들어있는 <username>.github.io. 앞으로 **output repo**라고 부른다

예제로 다음 2개의 저장소를 만들었다.

* 내용을 저장 : https://github.com/static-blog-sample/blog
* github pages를 저장 : https://github.com/static-blog-sample/static-blog-sample.github.io


## content repo ↔ output repo ⇒ git submodule

[@talha131][talha131-blog]에게 배운 편법이다.
content repo와 output repo를 git submodule로 엮는다. static html generator로 html을 생성하면 output repo로 데이터가 적절히 들어간다. 이것을 서버로 푸시하면 블로그에 새 글이 올라간다.

```bash
# content repo 에 위치한 상태
# output repo의 경우는 자기에 맞게 바꾼다

git submodule add https://github.com/static-blog-sample/static-blog-sample.github.io.git output
```

## 정적 사이트 생성기 붙이기

자신이 사용할 정적 사이트 생성기에 맞춰서 적절히 내부를 구성한다.
다른건 어떻게 설정하든 내가 알바 아니지만 생성 결과물이 **output**에 들어가도록 한다.
pelican을 이용한 설정 예제는 해당 블로그를 참고하면 된다.


## travis-ci

새로운 글이 푸시되었을때 travis-ci가 하고싶은 작업은 다음과 같다.

1. static html generator를 돌려서 html을 생성한다. html은 output에 들어간다
2. output repo의 내용을 커밋한 다음 푸시한다.
3. 참 쉽죠?

이를 하기 위해서는 몇가지 과정을 거쳐야한다.


### static html generator가 돌아갈 수 있는 환경 만들기.

jekyll을 쓰건 pelican을 쓰건 이런 static html generator은 travis-ci에 당연히 설치되어있지 않다.
.travis.yml에 해당 패키지를 설치하는 스크립트를 잊지말고 작성한다.

### GitHub Token

travis-ci에서 다른 저장소로 푸시를 하기 위해서는 token이 필요하다.
github profile -> [Applications](https://github.com/settings/applications)
으로 들어간다.
**Create new token** 을 누르고 적절히 token을 하나 만든다. 이 token을 기억해놓는다.

![Create new token](/static/create-token.png)

token은 얻었는데 이것을 ```.travis.yml```에 그냥 노출시키는건 말이 안되잖아?
그래서 [travis-ci는 token과 같이 중요한 정보를 암호화 시키는 방법][http://docs.travis-ci.com/user/encryption-keys/]을 제공한다.
루비 gem이 필요한 관계로 이것이 굴러가는 환경을 구축한다.
아래의 명령에서 repo-name은 자신한테 맞는것으로 바꾼다. 예를 들면 이 글의 경우는 ```static-blog-sample/static-blog-sample.github.io```이다.

```
gem install travis
travis encrypt GH_TOKEN=<token> -r <repo-name>

```

출력으로 ```secure: ".... encrypted data ...."``` 와 같은게 나온다. 이를 ```.travis.yml```에 집어넣는다.

### 빌드 스크립트 작성

travis-ci가 블로그를 받아서 수행할 작업을 작성한다. 세부 내용은 자신의 환경에 맞춰서 바꾸면된다.

```
# 정적 html 생성은 자신이 사용하는 환경에 맞춰서 바꾼다.
make publish
git config --global user.email "your-mail@gmail.com"
git config --global user.name "Travis"
cd output
git pull origin master
git checkout master
git add -f .
git commit -a -m "add new site content"
git push https://${GH_TOKEN}@github.com/static-blog-sample/static-blog-sample.github.io.git master
```


# Reference

* GitHub Pages : http://pages.github.com/
* [정적 웹사이트 생성기의 유혹][static-site-generator]
* wesleyhales.com : https://github.com/wesleyhales/wesleyhales.com
* https://github.com/talha131/onCrashReboot
* Disqus : http://disqus.com
* Pelican : http://blog.getpelican.com/

[github-custom-domain]: https://help.github.com/articles/setting-up-a-custom-domain-with-pages
[static-site-generator]: http://blog.nacyot.com/articles/2014-01-15-static-site-generator/
[talha131-blog]: https://github.com/talha131/onCrashReboot