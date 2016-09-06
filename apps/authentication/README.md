# django-rest-api authentication

## Facebook Social Login

먼저, testapp에 관리자/테스터로 등록이 되어있어야 함.

#### Environment Setting
로컬에서 서버를 연 후, localhost.3000won.com:접속포트/facebook/ 으로 접속하면 facebook 로그인 버튼이 뜸.
로그인 후, 토큰이 로그에 찍힌다(자바스크립트 FB.getAccessToken() 함수로 구할 수 있음).
localhost.3000won.com:접속포트/api-auth/      <<< POST를 보낸다( {"auth_token": (페북에서 받은 토큰)} )
자동으로 회원가입&로그인이 완료된다.
