import streamlit as st
import numpy as np
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyD7Q9NrYROJlKzY1sD0OzQo2NKMGXwQPyc')

st.text_input("Insira um local", key="loc1")
st.text_input("Insira outro local", key="loc2")

print(st.session_state.loc1)
print(st.session_state.loc2)

data1 = st.session_state.loc1 #'R Doutor José Maria 804'
data2 = st.session_state.loc2 #'Pátio de São Pedro'

if(data1 and data2):
    dist = gmaps.distance_matrix(data1, data2)['rows'][0]['elements'][0]


    if(dist['status'] == 'NOT_FOUND' or dist['status'] == 'ZERO_RESULTS'):
        st.text("Esse bar não existe")
    else:
        st.text(dist)


ruas = ['rua1', 'rua2', 'rua3', 'rua4', 'rua5']

string = ''
for i in range(len(ruas)):
    string += ruas[i] + ' --> '
    if(i == len(ruas) - 1):
        string += ruas[i]
st.text(string)
