# 웹 스크래핑 실습 및 DB 저장 프로젝트

## 개요

본 프로젝트는 웹 기반 데이터를 수집하고, 정제된 데이터를 CSV 또는 MySQL 데이터베이스에 저장하는 전 과정을 다룹니다. 뉴스 기사와 이미지 등 다양한 미디어 요소를 포함하며, Beautidulsoup을 사용한 웹 페이지 수집, 데이터 저장 실습을 목표로 합니다.

---

## 실습1: 뉴스 데이터 수집하기

### 목적
뉴스 기사 본문과 제목을 스크래핑하여 CSV로 저장하고, MySQL에 저장하는 과정을 실습합니다.

### 사용 파일
- `뉴스데이터수집_실습.ipynb`  
  └ 뉴스 기사 제목과 본문을 스크래핑하여 `news.csv` 생성  
- `뉴스데이터수집_sql_실습.ipynb`  
  └ `news.csv` 데이터를 MySQL 테이블에 저장

### 생성 파일
- `news.csv`  
  뉴스 제목(`title`)과 내용(`content`) 포함

---

## 실습2: 멀티미디어 데이터 수집하기

### 목적
영화 제목과 이미지 URL을 수집하고, 이미지 파일로 저장한 후 데이터베이스에 저장합니다.

### 사용 파일
- `멀티미디어_데이터수집.ipynb`  
  └ 영화 제목 및 이미지 URL 수집, 이미지 파일 저장  
- `멀티미디어_sql.ipynb`  
  └ 이미지 URL 데이터(`movie_images.csv`)를 MySQL에 저장

### 생성 파일
- `movie_images.csv`  
  영화 제목과 이미지 URL이 포함된 파일  
- `images/` 폴더  
  저장된 영화 이미지 (`.png` 형식)

---

## 실습3: NOL 뮤지컬 티켓 랭킹

### 목적
뮤지컬 랭킹 정보를 스크래핑하여 정제된 CSV 파일을 만들고, 데이터베이스에 저장합니다.

### 사용 파일
- `NOL뮤지컬티켓랭킹.ipynb`  
  └ 뮤지컬 순위, 제목, 장소, 예매율 수집 및 정제  
- `NOL뮤지컬티켓랭킹_sql.ipynb`  
  └ `musicals_cleaned.csv` 데이터를 MySQL에 저장

### 생성 파일
- `musicals_cleaned.csv`  
  컬럼: `rank`, `title`, `location`, `reservation_rate`

---

## 주요 기능

- **웹 스크래핑**  
  BeautifulSoup을 활용하여 뮤지컬 랭킹, 뉴스 콘텐츠, 영화 이미지 정보를 수집

- **데이터 전처리 및 정제**  
  CSV로 저장 전 불필요한 기호 제거, 텍스트 정제 및 형 변환 수행

- **CSV 저장**  
  `pandas.DataFrame.to_csv()`를 활용하여 구조화된 형태로 저장

- **MySQL 연동**  
  `pymysql`을 사용하여 데이터베이스에 테이블 생성 및 다중 레코드 삽입

- **이미지 처리**  
  영화 제목을 파일명으로 한 이미지 저장 (Pillow 활용)

---

## 요구사항

- Python 3.8 이상
- MySQL 서버 설치 및 사용자 접근 권한 설정 필요

---

## 실행 순서 예시

1. **데이터 수집**
   - `NOL뮤지컬티켓랭킹.ipynb`
   - `뉴스데이터수집_실습.ipynb`
   - `멀티미디어_데이터수집.ipynb`

2. **CSV 저장 결과 확인**
   - `musicals_cleaned.csv`, `news.csv`, `movie_images.csv`

3. **MySQL 저장**
   - `NOL뮤지컬티켓랭킹_sql.ipynb`
   - `뉴스데이터수집_sql_실습.ipynb`
   - `멀티미디어_sql.ipynb`

---

## 데이터 출처

- [NOL 뮤지컬 랭킹](https://tickets.interpark.com/contents/ranking?genre=MUSICAL)
- [MovieChart 영화 순위](https://www.moviechart.co.kr/rank/realtime/index/image)
- [주요 뉴스 사이트 본문](https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=09&plink=RSSREADER)