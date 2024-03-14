import streamlit as st
import matplotlib as plt
import seaborn as sb
import pandas as pd
import numpy as np
import requests

st.title('Pokemon Explorer!')

def get_total_count():
    url = f'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokemon = response.json()
    return pokemon['count']

def get_details(poke_number):
	try:
		url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
		response = requests.get(url)
		pokemon = response.json()
		return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['moves'],  pokemon['sprites'], pokemon['cries']

	except:
		return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN
    
def extract_keys(data, parent_key='', sep='/'):
    keys = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        keys.append(new_key)
        if isinstance(v, dict):
            keys.extend(extract_keys(v, new_key, sep=sep))
    return keys	

def display_pokemon_info(name, height, weight, moves_count):
    st.markdown(f"### **Name:** {name.upper()}")
    st.markdown(f"**Height:** {height} m")
    st.markdown(f"**Weight:** {weight} kg")
    st.markdown(f"**Move Count:** {moves_count}")

pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=get_total_count()
						   )

name, height, weight, moves_count,moves, pokemon_sprites, cries = get_details(pokemon_number)

if name != 'Error':
    display_pokemon_info(name, height, weight,moves_count)
    all_image_keys = extract_keys(pokemon_sprites)
    selected_image_key = st.selectbox("Select Image key", all_image_keys)
    if pokemon_sprites[selected_image_key]:
        
        st.image(pokemon_sprites[selected_image_key])
    else:
         st.write('No Image available, Please select different image key')
    all_moves = [move["move"]["name"] for move in moves]
    selected_move_key = st.selectbox("List of types of Moves", all_moves)

st.write(f'Move Count: {moves_count}')
# Get all keys

height_data= pd.DataFrame({'Pokemon': ['Weedle', name, 'Victoreble'], 
			  'Height': [30,height, 170]})
colors =['lightblue', 'lightpink', 'lightgreen']
graph = sb.barplot(data = height_data,
				   x= 'Pokemon',
				   y = 'Height',
				   palette = colors)
st.pyplot(graph.figure)