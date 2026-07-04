import streamlit as st
import requests

api_url = 'http://127.0.0.1:9000/predict'

st.title('Diabetes Scan Project')

Pregnancies = st.number_input('Количество беременностей', min_value=0, max_value=20, value=0, step=1)
Glucose = st.number_input('Уровень глюкозы', min_value=0, max_value=300, value=100, step=1)
BloodPressure = st.number_input('Артериальное давление', min_value=0, max_value=200, value=70, step=1)
SkinThickness = st.number_input('Толщина кожной складки', min_value=0.0, max_value=100.0, value=20.0, step=1.0)
Insulin = st.number_input('Уровень инсулина', min_value=0.0, max_value=900.0, value=80.0, step=1.0)
BMI = st.number_input('Индекс массы тела (BMI)', min_value=0.0, max_value=70.0, value=25.0, step=0.1)
DiabetesPedigreeFunction = st.number_input('Наследственная предрасположенность (DPF)', min_value=0.0, max_value=3.0, value=0.5, step=0.01)
Age = st.number_input('Возраст', min_value=0, max_value=120, value=30, step=1)

diabetes_data = {
    "Pregnancies": Pregnancies,
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    "SkinThickness": SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age,
}

if st.button('Предсказать'):
    try:
        answer = requests.post(api_url, json=diabetes_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(
                f"Диабет: {'Да' if result.get('diabetes') else 'Нет'}, "
                f"вероятность: {result.get('probability')}"
            )
        else:
            st.error(f"Ошибка: {answer.status_code}")
    except requests.exceptions.RequestException:
        st.error("Не удалось соединиться к API")