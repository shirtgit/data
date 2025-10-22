# 🌤️ 날씨 웹 애플리케이션

OpenWeather API를 사용한 Streamlit 기반 실시간 날씨 정보 웹 애플리케이션입니다.

## 🚀 기능

- **실시간 날씨 조회**: 전 세계 도시의 현재 날씨 정보
- **5일 예보**: 시간별 날씨 예보 정보
- **직관적인 UI**: Streamlit을 활용한 사용자 친화적 인터페이스
- **상세 정보**: 온도, 습도, 기압, 바람, 가시거리 등 다양한 날씨 데이터
- **한국어 지원**: 날씨 설명 한국어 표시

## 📋 요구사항

- Python 3.7 이상
- OpenWeather API 키

## 🛠️ 로컬 설치 및 실행

### 1. 저장소 클론 및 이동
```bash
git clone <repository-url>
cd data
```

### 2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. API 키 설정
`.streamlit/secrets.toml` 파일에서 OpenWeather API 키를 설정하세요:
```toml
OPENWEATHER_API_KEY = "your-api-key-here"
```

### 4. 애플리케이션 실행
```bash
streamlit run app.py
```

## 🚀 Streamlit Cloud 배포

### 1. GitHub 저장소 준비
```bash
git add .
git commit -m "날씨 앱 배포 준비"
git push origin main
```

### 2. Streamlit Cloud 배포
1. [Streamlit Cloud](https://share.streamlit.io/)에 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소 선택: `your-username/data`
5. Branch: `main`
6. Main file path: `app.py`
7. "Deploy!" 클릭

### 3. Secrets 설정 (중요!)
배포 후 앱 설정에서 다음 secrets를 추가해야 합니다:

**앱 대시보드 → Settings → Secrets**
```toml
OPENWEATHER_API_KEY = "d67076f84b91e30c008fe16e891ecc2e"
```

### 4. 배포 완료
- 배포가 완료되면 공개 URL을 받게 됩니다
- 예: `https://your-app-name.streamlit.app`

## 📁 프로젝트 구조

```
data/
├── app.py              # 메인 Streamlit 애플리케이션
├── config.py           # API 키 및 설정 관리
├── requirements.txt    # 필요한 Python 패키지
└── README.md          # 프로젝트 설명서
```

## 🔧 주요 함수

### `get_weather_data(city_name, api_key)`
- 현재 날씨 정보를 조회하는 함수
- OpenWeather Current Weather API 사용

### `get_forecast_data(city_name, api_key)`
- 5일 예보 정보를 조회하는 함수
- OpenWeather 5 Day Weather Forecast API 사용

### `display_current_weather(weather_data)`
- 현재 날씨 정보를 화면에 표시하는 함수

### `display_forecast(forecast_data)`
- 예보 정보를 표 형태로 표시하는 함수

## 🌍 지원하는 도시

- 전 세계 모든 도시 (영어명)
- 한국 주요 도시 (한국어/영어명 모두 지원)
  - 서울 (Seoul)
  - 부산 (Busan)
  - 인천 (Incheon)
  - 대구 (Daegu)
  - 광주 (Gwangju)
  - 대전 (Daejeon)
  - 울산 (Ulsan)

## 📊 표시되는 정보

### 현재 날씨
- 현재 온도 및 체감 온도
- 최고/최저 온도
- 습도
- 기압
- 바람 속도
- 날씨 설명
- 가시거리

### 5일 예보
- 날짜 및 시간
- 예상 온도
- 날씨 상태
- 습도
- 바람 정보

## 🔗 API 정보

이 애플리케이션은 [OpenWeatherMap API](https://openweathermap.org/api)를 사용합니다.

- Current Weather Data API
- 5 Day / 3 Hour Forecast API

## 📝 사용 방법

1. 웹 애플리케이션이 실행되면 왼쪽 사이드바에서 도시명을 입력합니다.
2. "날씨 조회" 버튼을 클릭합니다.
3. 현재 날씨 정보와 5일 예보를 확인합니다.
4. 다른 도시의 날씨를 조회하려면 도시명을 변경하고 다시 조회합니다.

## 🛡️ 보안 고려사항

- **로컬 개발**: API 키는 `.streamlit/secrets.toml` 파일에 저장 (Git 추적되지 않음)
- **배포 환경**: Streamlit Cloud의 Secrets 관리 기능 사용
- `.gitignore`에 의해 민감한 정보가 Git에 커밋되지 않도록 보호

## ⚠️ 배포 시 주의사항

1. **Secrets 설정 필수**: 배포 후 반드시 Streamlit Cloud에서 API 키를 설정해야 합니다
2. **파일 구조 확인**: `app.py`가 루트 디렉토리에 있어야 합니다
3. **requirements.txt**: 모든 필요한 패키지가 명시되어 있어야 합니다
4. **API 키 유효성**: OpenWeather API 키가 유효하고 활성화되어 있어야 합니다

## 🤝 기여

버그 리포트나 기능 제안은 이슈를 통해 제출해주세요.

## 📄 라이선스

MIT License