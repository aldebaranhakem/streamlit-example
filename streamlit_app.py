import streamlit as st
"""
# Kalkulator sederhana

berikut adalah program sederhana untuk menjalankan program kalkulator menggunakan teknik python sederhana
serta pengimplementasian untuk membuat ui pada kalkulator yang ada (sederhana)

"""

'''kalkulator penjumlahan'''

input_1 = st.number_input('Masukan angka 1:', min_value=0)
input_2 = st.number_input('Masukan angka 2:', min_value=0)

Tambah = input_1 + input_2 
Kurang = input_1 - input_2 
Kali = input_1 * input_2

Tambah, Kurang, Kali = st.columns([1,1,1])

with Tambah:
  if st.button('+'):
     st.subheader('Hasil nya', Tambah)

with Kurang:
  if st.button('-'):
     st.subheader('Hasil nya', Kurang)
  
with Kali:
  if st.button('X'):
     st.subheader('Hasil nya', Kali)

