import streamlit as st
import requests
import pandas as pd
from config import OPENWEATHER_API_KEY
from datetime import datetime
import json

# Streamlit 페이지 설정
st.set_page_config(
    page_title="날씨 웹 애플리케이션",
    page_icon="🌤️",
    layout="wide"
)

def get_weather_data(city_name, api_key):
    """
    OpenWeather API를 사용하여 날씨 데이터를 가져오는 함수
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # 섭씨 온도
        'lang': 'kr'  # 한국어
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"날씨 정보를 가져오는데 실패했습니다: {e}")
        return None

def get_forecast_data(city_name, api_key):
    """
    OpenWeather API를 사용하여 5일 예보 데이터를 가져오는 함수
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'kr'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"예보 정보를 가져오는데 실패했습니다: {e}")
        return None

def display_current_weather(weather_data):
    """
    현재 날씨 정보를 표시하는 함수
    """
    if weather_data:
        # 메인 정보
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="온도", 
                value=f"{weather_data['main']['temp']:.1f}°C",
                delta=f"체감온도 {weather_data['main']['feels_like']:.1f}°C"
            )
        
        with col2:
            st.metric(
                label="습도", 
                value=f"{weather_data['main']['humidity']}%"
            )
        
        with col3:
            st.metric(
                label="기압", 
                value=f"{weather_data['main']['pressure']} hPa"
            )
        
        with col4:
            st.metric(
                label="바람", 
                value=f"{weather_data['wind']['speed']} m/s"
            )
        
        # 날씨 설명
        weather_desc = weather_data['weather'][0]['description']
        st.subheader(f"현재 날씨: {weather_desc.title()}")
        
        # 추가 정보
        st.write(f"**최고/최저 온도:** {weather_data['main']['temp_max']:.1f}°C / {weather_data['main']['temp_min']:.1f}°C")
        if 'visibility' in weather_data:
            st.write(f"**가시거리:** {weather_data['visibility']/1000:.1f} km")

def display_forecast(forecast_data):
    """
    5일 예보를 표시하는 함수
    """
    if forecast_data:
        st.subheader("5일 예보")
        
        # 예보 데이터 처리
        forecast_list = []
        for item in forecast_data['list'][:5]:  # 5개 항목만 표시
            forecast_list.append({
                '날짜': datetime.fromtimestamp(item['dt']).strftime('%m월 %d일 %H시'),
                '온도': f"{item['main']['temp']:.1f}°C",
                '날씨': item['weather'][0]['description'],
                '습도': f"{item['main']['humidity']}%",
                '바람': f"{item['wind']['speed']} m/s"
            })
        
        # 데이터프레임으로 표시
        df = pd.DataFrame(forecast_list)
        st.dataframe(df, use_container_width=True)

def main():
    """
    메인 애플리케이션 함수
    """
    st.title("🌤️ 날씨 웹 애플리케이션")
    st.markdown("OpenWeather API를 사용한 실시간 날씨 정보")
    
    # 사이드바
    st.sidebar.header("설정")
    
    # 도시 입력
    city_name = st.sidebar.text_input(
        "도시 이름을 입력하세요:", 
        value="Seoul",
        help="한국어 또는 영어로 도시명을 입력할 수 있습니다."
    )
    
    # 검색 버튼
    if st.sidebar.button("날씨 조회", type="primary"):
        if city_name:
            with st.spinner("날씨 정보를 가져오는 중..."):
                # 현재 날씨 조회
                weather_data = get_weather_data(city_name, OPENWEATHER_API_KEY)
                
                if weather_data:
                    st.success(f"{weather_data['name']}, {weather_data['sys']['country']}의 날씨 정보")
                    
                    # 현재 날씨 표시
                    display_current_weather(weather_data)
                    
                    # 예보 정보 조회 및 표시
                    forecast_data = get_forecast_data(city_name, OPENWEATHER_API_KEY)
                    if forecast_data:
                        display_forecast(forecast_data)
                else:
                    st.error("날씨 정보를 찾을 수 없습니다. 도시명을 확인해주세요.")
        else:
            st.warning("도시명을 입력해주세요.")
    
    # 정보 섹션
    st.sidebar.markdown("---")
    st.sidebar.info(
        "💡 **사용법:**\n"
        "1. 도시명을 입력하세요\n"
        "2. '날씨 조회' 버튼을 클릭하세요\n"
        "3. 현재 날씨와 예보를 확인하세요"
    )
    
    # 기본 화면 (검색 전)
    if 'weather_searched' not in st.session_state:
        st.info("👈 왼쪽 사이드바에서 도시명을 입력하고 날씨를 조회해보세요!")
        
        # 주요 도시들 예시
        st.subheader("주요 도시 예시")
        cities = ["Seoul", "Busan", "Incheon", "Daegu", "Gwangju", "Daejeon", "Ulsan"]
        cols = st.columns(len(cities))
        
        for i, city in enumerate(cities):
            with cols[i]:
                if st.button(city, key=f"city_{city}"):
                    st.session_state.selected_city = city
                    st.rerun()

if __name__ == "__main__":
    main()