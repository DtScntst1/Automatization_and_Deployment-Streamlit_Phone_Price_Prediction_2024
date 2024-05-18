import streamlit as st
import joblib

# Title of the application
st.title("Cep Telefonu Tahmin Uygulaması")

# Header
st.header("Cep Telefonunuzun fiyatını tahmin edin.")

# Subheader
st.subheader("Bu uygulamayı kullanarak cep telefonunuzun değerini öğrenebilirsiniz.")

st.image("cep telefonu.jpg", caption="Cep Telefonu", width=400)

st.write("İlgilendiğiniz cep telefonunun tahmini piyasada değerini aşağıda görebilirsiniz.")

top_7_feature_names = joblib.load("top_7_feature_names.joblib")

import streamlit as st
import pandas as pd

# Başlık
st.header('Telefon Detaylarını Girin')

# Marka seçimi
brand = st.selectbox('Marka', ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo'])

# Model seçimi için örnek modeller
model_dict = {
    'Samsung': ['Samsung Galaxy S21', 'Samsung Galaxy Note 20', 'Samsung Galaxy A52'],
    'Apple': ['Apple iPhone 13', 'Apple iPhone 12', 'Apple iPhone SE'],
    'Huawei': ['Huawei P40', 'Huawei Mate 40', 'Huawei Y9a'],
    'Xiaomi': ['Xiaomi Mi 11', 'Xiaomi Redmi Note 10', 'Xiaomi Poco X3'],
    'Oppo': ['Oppo Reno5', 'Oppo A54', 'Oppo Find X3 Pro']
}

model = st.selectbox('Model', model_dict[brand])
ram = st.number_input('RAM (GB)', min_value=1, value=4)
camera_mp = st.number_input('Kamera (MP)', min_value=1, value=12)
screen_size = st.slider('Ekran Boyutu (inç)', min_value=4.0, max_value=7.0, step=0.1, value=6.0)
battery_capacity = st.number_input('Batarya Kapasitesi (mAh)', min_value=1000, max_value=6000, step=100, value=4000)
storage = st.number_input('Depolama (GB)', min_value=8, value=64)

# Kullanıcı girdilerini bir DataFrame'e koyma
sample_one = pd.DataFrame({
    'Model': [model],
    'RAM': [ram],
    'Brand': [brand],
    'Camera_MP': [camera_mp],
    'Screen_Size': [screen_size],
    'Battery_Capacity': [battery_capacity],
    'Storage': [storage]
})

# Marka ve diğer kategorik değişkenler için kodlama (örnek olarak)
brand_mapping = {'Samsung': 0, 'Apple': 1, 'Huawei': 2, 'Xiaomi': 3, 'Oppo': 4}
sample_one['Brand'] = sample_one['Brand'].map(brand_mapping)

# Model fiyat etkisi (örnek)
model_price_effect = {
    'Samsung Galaxy S21': 200, 'Samsung Galaxy Note 20': 180, 'Samsung Galaxy A52': 150,
    'Apple iPhone 13': 300, 'Apple iPhone 12': 250, 'Apple iPhone SE': 200,
    'Huawei P40': 180, 'Huawei Mate 40': 160, 'Huawei Y9a': 140,
    'Xiaomi Mi 11': 160, 'Xiaomi Redmi Note 10': 140, 'Xiaomi Poco X3': 120,
    'Oppo Reno5': 150, 'Oppo A54': 130, 'Oppo Find X3 Pro': 200
}

# Fiyat tahmini fonksiyonu (örnek)
def predict_price(sample):
    base_price = 300  # Temel fiyat (örnek olarak)
    
    # Özelliklerin ağırlıkları (örnek)
    ram_weight = 50
    camera_weight = 20
    screen_weight = 30
    battery_weight = 0.1
    storage_weight = 2
    brand_weight = 100  # Marka etkisi (örnek)

    # Modelin fiyat üzerindeki etkisi
    model_effect = model_price_effect.get(sample['Model'][0], 0)

    # Fiyat hesaplama
    price = (
        base_price +
        model_effect +
        sample['RAM'][0] * ram_weight +
        sample['Camera_MP'][0] * camera_weight +
        sample['Screen_Size'][0] * screen_weight +
        sample['Battery_Capacity'][0] * battery_weight +
        sample['Storage'][0] * storage_weight +
        sample['Brand'][0] * brand_weight
    )
    
    return round(price, 2)

# Kullanıcı girdilerini işleme ve tahmin etme
if st.button('Fiyatı Tahmin Et'):
    predicted_price = predict_price(sample_one)
    st.write(f"TAHMİNİ TELEFON FİYATI: ${predicted_price}")
    st.title(f"${predicted_price}")




