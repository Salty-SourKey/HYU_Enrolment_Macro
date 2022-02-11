# HYU Enrolment Macro

한양대학교 수강 신청 중 신청 인원의 변동을 주기적으로 감시하고
빈자리가 났을 시 자동으로 수강 신청하는 매크로입니다.

**Requirement**
 - Google Chrome (없으면 안 됨)
 - Python `https://www.python.org/downloads/` (저는 3.7.3 사용했는데 버전은 상관없을 듯)
 - Selenium `pip install selenium`
 - Web Driver Manager `pip install webdriver-manager`
 - Chrome Driver `https://sites.google.com/a/chromium.org/chromedriver/downloads`

## 보소

#### 사용자 설정

 1. HYU_Enrolment_Macro 파일을  편집기로 열고 한양대학교 포탈 아이디 및 비밀번호 입력

	- user_id = '여기에 아이디 입력'
	- user_pw = '여기에 비밀번호 입력'

2. HYU_Enrolment_Macro 파일을 실행시키고 무한으로 즐기면 됨



## 몰?루

 - 만약 cmd창에 정체불명의 긴 에러가 나온다면 아직 창이 뜨지도 않았는데 명령을 실행하다 그런 것이니 컴퓨터 환경에 맞게 time.sleep(#)의 상수를 조정해야한다.

 - 새로고침 빈도가 느리다면 맨 밑 time.sleep(#)의 상수를 더 작은 거로 사용하면 된다.
 
 - 물론 내가 쓰려고 만든 프로그램이지만 쓰다가 불이익은 내가 책임은 지지 않는다.
	 > **With great power comes great responsibility.**  - Benjamin Parker