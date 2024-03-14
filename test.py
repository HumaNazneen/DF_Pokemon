import streamlit as st
import matplotlib as plt
import seaborn as sb
import pandas as pd
import numpy as np
import requests

st.title('Pokemon Explorer!')

def get_details(poke_number):
	try:
		url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
		response = requests.get(url)
		pokemon = response.json()
		#st.write(pokemon)
		return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites'], pokemon['cries']

	except:
		return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN
	

pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=150
						   )

name, height, weight, moves, images, cries = get_details(pokemon_number)
image_dream_world = images['other']['dream_world']['front_default']
image_official_artwork = images['other']['official-artwork']['front_shiny']
image_showdown = images['other']['showdown']['back_shiny']
image_back_default = images['back_default']
cries_latest = cries['latest']
cries_legacy = cries['legacy']
height_data= pd.DataFrame({'Pokemon': ['Weedle', name, 'Victoreble'], 
			  'Height': [30,height, 170]})
colors =['lightblue', 'lightpink', 'lightgreen']
graph = sb.barplot(data = height_data,
				   x= 'Pokemon',
				   y = 'Height',
				   palette = colors)

st.write(f'Name: {name}')
st.write(f'Height: {height}')
st.write(f'Weight: {weight}')
st.write(f'Move Count: {moves}')
st.image(image_back_default, use_column_width=False,  width= 200 )
st.image(image_dream_world, use_column_width=False,  width= 100 )
st.image(image_official_artwork, use_column_width=False,  width= 100 )
st.image(image_showdown, use_column_width=False,  width= 100 )
st.write('cries_latest')
st.audio(cries_latest, format='audio/ogg')
st.write('cries_legacy')
st.audio(cries_legacy, format='audio/ogg')
st.pyplot(graph.figure)