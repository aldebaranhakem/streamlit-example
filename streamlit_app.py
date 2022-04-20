import streamlit as st
"""
# Kalkulator sederhana

berikut adalah program sederhana untuk menjalankan program kalkulator menggunakan teknik python sederhana
serta pengimplementasian untuk membuat ui pada kalkulator yang ada (sederhana)

"""

'''kalkulator penjumlahan'''

input_1 = st.number_input('Masukan angka 1:')
input_2 = st.number_input('Masukan angka 2:')

Tambah = st.button('+', input_1 + input_2),  
Kurang = st.button('-', input_1 - input_2), 
Kali = st.button('X', input_1*input_2)

st.write('Hasil nya',float(Tambah)) 
