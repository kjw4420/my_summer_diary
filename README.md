# 나의 **여름 방학** 일기

## :bookmark_tabs: 프로젝트 설명
**Target: 이런 사람에게 추천해요** 🎯<br>
 📌 짧은 여름 방학 일정 관리를 하고 싶어요!<br>
 📌 긴 일기를 쓰는 건 부담스러워, 짧게 오늘을 기록하고 싶어!<br>
 📌 일기에 그림도 그리고 싶고 사진도 넣고 싶어!<br>
 📌 다양한 전시회 정보를 알고싶어!<br><br>

**나의 알찬 여름 방학 보내는 법** ❗️  <br>
 ✔️ To Do List로 오늘의 할 일 기록 <br>
 ✔️ Summer Bucket List로 여름 방학 기간 동안 하고 싶은 일 기록  <br>
 ✔️ 그림 일기로 오늘을 되돌아 보기<br><br>


<img width="811" alt="스크린샷 2023-07-17 오전 1 47 55" src="https://github.com/kjw4420/my_summer_diary/assets/97749184/10050cc3-f7cb-43ef-81f2-27dab6a322cc"><br>
<img width="918" alt="스크린샷 2023-07-17 오전 2 33 20" src="https://github.com/kjw4420/my_summer_diary/assets/97749184/b4d3d7e2-4b26-492e-9d32-300f2b2a1885"><br>
<img width="918" alt="스크린샷 2023-07-17 오전 2 33 30" src="https://github.com/kjw4420/my_summer_diary/assets/97749184/dbea4fa4-09dc-424a-91de-bdeaf3792500"><br>


  최근 SNS나 길거리를 지나가다 보면 다양한 주제의 전시회가 열리고 있고, 그에 대한 사람들의 관심도도 높아지고 있다. 그러나 전시회에 대한 정보는 획일적 광고가 대부분이며, 직접 찾아보지 않는 이상 개인이 관심있는 분야(취향)에서 열리고 있는 전시회에 대한 정보를 알기 어렵다. 또 SNS에 미숙한 세대는 관련 정보를 찾기가 더욱 힘들다. 따라서 본 프로젝트에서는 회원에 따라 취향에 맞는 전시회를 추천 및 필터별로 정렬해 문화인에게 전시회에 대한 **‘접근성’**, **‘다앙성**을 제공하는 것을 목표로 한다.

## 📗 주요 기능
🔍**회원가입 및 로그인**<br>
회원가입 페이지에 아이디, 비밀번호, 이름, 닉네임을 받아와 서버를 통해 ExhibitionDB에 있는 Accounts Table에 저장한 후 로그인을 진행한다. 로그인 창에 입력한 아이디와 비밀번호가 Accounts Table에 있는 정보와 일치하면 로그인이 허가된다.<br><br>
🔍**취향분석(분류; 회원 취향 분석)**<br>
로그인을 하면 취향분석 테스트를 할 수 있는 링크가 생성되고 이를통해 로그인한 회원이 선택하는 대답에 따라서 취향(ex, 현대적, 전통적 등)을 분석하여 Exhibition DB에 있는 Accounts Table에 들어있는 키워드로 분류하여 회원정보와 함께 저장한다.<br><br>
🔍**필터정렬(읽기; 최신순, 취향별)**<br>
Exhibition_detail Table로부터 등록된 전시회 리스트를 받아온 후 필터를 사용해 취향별 (키워드), 최신순으로 정렬하고 이를 사용자에게 보여준다.<br><br>
🔍**전시정보<사용자>(삽입, 읽기, 상세정보)**<br>
사용자가 전시회 리스트에서 누른 전시의 상세정보를 보여준다. 상세정보는 전시회 이름, 전시회 상세설명, 장소, 가격, 공식홈페이지 링크, 사진 촬영 가능 여부를 포함한다.<br><br>
🔍**전시정보<관리자>(삽입, 삭제, 갱신(수정); 상세정보)**<br>
전시정보를 등록하는 것으로 전시회 이름, 전시회 상세설명, 장소, 가격, 공식홈페이지 링크, 사진 촬영 가능 여부에 대한 정보를 삽입, 삭제, 갱신(수정)이 가능하도록 한다.<br><br>


## 👩🏻‍💻 멤버


### Front-end

|               | github                             |
| ------------- | ---------------------------------- |
| 김연희 |https://github.com/kjw4420    |
| 박현지       |         |
| 유나현      |         |

### back-end

|               | github                             |
| ------------- | ---------------------------------- |
| 김지원  |https://github.com/kjw4420    |
| 조서현        |         |

### 디자인

김연희, 박현지

## :hammer_and_wrench: 사용 기술

### Front-end

**프로그래밍 언어**<br>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/>
<br>


### Back-end

**언어**<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
 <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/>
**프레임워크/라이브러리**<br>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/> <br>

**데이터베이스**<br>
<img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=Sqlite&logoColor=white">


