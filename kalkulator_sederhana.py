import streamlit as st
"""
## Kalkulator Sederhana

berikut adalah program sederhana untuk menjalankan program kalkulator menggunakan teknik python sederhana
serta pengimplementasian untuk membuat ui pada kalkulator yang ada (sederhana)

"""

'''kalkulator penjumlahan'''

input_1 = st.number_input('Masukan angka 1:', min_value=0)
input_2 = st.number_input('Masukan angka 2:', min_value=0)

Tambah = input_1 + input_2 
Kurang = input_1 - input_2 
Kali = input_1 * input_2
Bagi = input_1 : input_2

total_tambah = float(Tambah)
total_kurang = float(Kurang)
total_kali = float(Kali)
total_bagi = float(Bagi)

Tambah, Kurang, Kali, Bagi = st.columns([1,1,1,1])

with Tambah:
  if st.button('+'):
#      st.write('Hasil nya', total_tambah)

with Kurang:
  if st.button('-'):
#      st.write('Hasil nya', total_kurang)
  
with Kali:
  if st.button('X'):
#      st.write('Hasil nya', total_kali)

with Bagi:
  if st.button(':'):
#      st.write('Hasil nya', total_bagi)

Nums = [total_tambah, total_kurang, total_kali, total_bagi]
st.subheader(f'Hasil nya : {Nums}')

