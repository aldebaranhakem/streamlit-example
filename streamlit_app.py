import streamlit as st
"""
# Kalkulator sederhana

berikut adalah program sederhana untuk menjalankan program kalkulator menggunakan teknik python sederhana
serta pengimplementasian untuk membuat ui pada kalkulator yang ada (sederhana)

"""

'''kalkulator penjumlahan'''

A = st.input(int('Insert a number:'))
B = st.input(int('Insert a number:'))

Tambah = st.button(f'Tambah {A + B}') 
Kurang = st.button(f'Kurang {A - B}')
Bagi = st.button(f'Bagi {A : B}')
Kali = st.button(f'Kali {A * B}')

st.write(f'Hasil tambahan:{Tambah}')
st.write(f'Hasil tambahan:{Kurang}')
st.write(f'Hasil tambahan:{Bagi}')
st.write(f'Hasil tambahan:{Kali}')
