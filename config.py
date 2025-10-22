import streamlit as st
import os

# OpenWeather API 설정
# 배포 시에는 Streamlit secrets 사용, 로컬에서는 환경변수 또는 기본값 사용
def get_api_key():
    """API 키를 안전하게 가져오는 함수"""
    try:
        # Streamlit Cloud에서는 st.secrets 사용
        return st.secrets["OPENWEATHER_API_KEY"]
    except:
        # 로컬 개발 시에는 환경변수 또는 기본값 사용
        return os.getenv("OPENWEATHER_API_KEY", "d67076f84b91e30c008fe16e891ecc2e")

OPENWEATHER_API_KEY = get_api_key()

# API 기본 설정
BASE_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER_URL = BASE_URL + "weather"
FORECAST_URL = BASE_URL + "forecast"

# 기본 설정
DEFAULT_UNITS = "metric"  # 섭씨 온도
DEFAULT_LANG = "kr"  # 한국어