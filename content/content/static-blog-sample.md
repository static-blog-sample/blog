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