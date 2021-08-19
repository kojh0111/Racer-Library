# 도서관 대출 서비스

## Flask를 활용한 도서관 대출 페이지 만들기

- [ ] **메인 페이지**
    - [x] DB상의 모든 책 정보 가져오기(페이지네이션 기능 이용 - 페이지 당 8권 표현)
    - [x] DB상의 현재 재고 표기
    - [x] 책 이름 클릭시 책 소개 페이지 이동
    - [ ] 평점은 모든 평점의 평균값, 숫자 일의 자리로 반올림

<br>

- [x] **회원가입**
    - [x] username을 받아야 함(한글 또는 영어만 허용)
    - [x] id는 email 형식으로 받음
    - [x] 비밀번호와 비밀번호 확인이 일치해야 함(영문, 숫자, 특수문자 중 2종류 이상을 조합 & 10자리 이상 or 영문, 숫자, 특수문자을 조합 & 8자리 이상)

<br>

- [ ] **로그인**
    - [ ] id, password는 필수 입력 사항(id는 email형식만 입력 받음 & password는 8자리 이상)
    - [x] 유저로부터 id, password 정보를 입력받아 로그인
    - [x] 로그인한 유저에 대해 session으로 관리

<br>

- [x] **로그아웃**
    - [x] 로그인한 유저에 대해 로그아웃
    - [x] session에서 제거

<br>

- [x] **책 소개**
    - [x] 메인 페이지로부터 접근
    - [x] 책에 대한 소개 출력

<br>

- [ ] **리뷰**
    - [ ] 가장 최신 댓글부터 정렬하여 출력
    - [ ] 댓글과 평가 점수는 모두 필수 입력 사항

<br>

- [ ] **대여하기**
    - [x] 메인 페이지의 대여하기 버튼을 클릭하여 대여
    - [ ] 현재 DB 상에 책에 존재하는 경우, 책을 대여하고 책의 권수를 -1로 변환
    - [x] 현재 DB 상에 책이 존재 하지 않는 경우, 책 대여 불가
    - [ ] 대여가 불가능한 경우 메시지 반환

<br>

- [ ] **대여기록**
    - [ ] 반납한 책을 출력
    - [ ] 대여일자와 반납일자 표기

<br>

- [ ] **반납하기**
    - [ ] 로그인한 유저가 대여한 모든 책 출력
    - [ ] 대여날짜 표기

