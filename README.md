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

## 🛠️ 설치 및 실행

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
`config.py` 파일에서 OpenWeather API 키를 확인하거나 수정하세요:
```python
OPENWEATHER_API_KEY = "your-api-key-here"
```

### 4. 애플리케이션 실행
```bash
streamlit run app.py
```

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

- API 키는 `config.py` 파일에 저장되어 있습니다.
- 실제 배포 시에는 환경 변수를 사용하여 API 키를 관리하는 것을 권장합니다.

## 🤝 기여

버그 리포트나 기능 제안은 이슈를 통해 제출해주세요.

## 📄 라이선스

MIT License