# Execute in terminal before running the script: "ollama pull llama3.2"

import streamlit as st
import folium
from geopy.geocoders import Nominatim
from langchain.llms import Ollama
from streamlit_folium import st_folium
import re

# Initialize the geocoder
geolocator = Nominatim(user_agent="map_generator")

# Function to extract potential location names using basic regex matching
def extract_locations(text):
    # A basic regex to match words that could represent locations (e.g., capitalized words)
    possible_locations = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    # Use set to remove duplicates and filter using geocoding
    return [loc for loc in set(possible_locations) if is_geographical_name(loc)]

# Function to validate if a name is a geographical location using geopy
def is_geographical_name(location_name):
    try:
        # Attempt to geocode the location name to see if it is valid
        location = geolocator.geocode(location_name)
        return location is not None
    except:
        return False

# Function to geocode location names to latitude and longitude
def geocode_location(location_name):
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Function to generate the interactive map with optional lines
def generate_map(locations, draw_lines=False):
    geocoded_locations = []
    for loc in locations:
        lat, lon = geocode_location(loc)
        if lat is not None and lon is not None:
            geocoded_locations.append({'name': loc, 'lat': lat, 'lon': lon})
        else:
            st.warning(f"Could not find coordinates for {loc}")

    if not geocoded_locations:
        st.error("No valid locations to plot on the map.")
        return None

    # Center the map on the average latitude and longitude
    avg_lat = sum(loc['lat'] for loc in geocoded_locations) / len(geocoded_locations)
    avg_lon = sum(loc['lon'] for loc in geocoded_locations) / len(geocoded_locations)
    map_obj = folium.Map(location=[avg_lat, avg_lon], zoom_start=2)

    # Add markers to the map
    for loc in geocoded_locations:
        folium.Marker(
            [loc['lat'], loc['lon']],
            popup=folium.Popup(loc['name'], parse_html=True)
        ).add_to(map_obj)

    # Draw lines if requested
    if draw_lines and len(geocoded_locations) > 1:
        line_points = [(loc['lat'], loc['lon']) for loc in geocoded_locations]
        folium.PolyLine(line_points, color='blue', weight=2.5, opacity=1).add_to(map_obj)

    return map_obj

def main():
    st.title("Prompt to Map Generator")
    st.write("Enter a prompt that includes locations you want to map.")

    # Initialize the Ollama LLM with the llama3.2 model
    llm = Ollama(model="llama3.2")

    # Use Streamlit's session state to store the map data
    if 'map_data' not in st.session_state:
        st.session_state['map_data'] = None

    # Custom system prompt
    system_prompt = "You are a helpful assistant that extracts location names and can process commands for mapping. Recognize phrases like 'draw lines' to indicate that the user wants lines connecting locations on the map."
    
    prompt = st.text_area("Enter your prompt:", height=100)

    draw_lines = False
    if 'draw lines' in prompt.lower():
        draw_lines = True

    if st.button("Generate Map"):
        with st.spinner("Processing the prompt with the language model..."):
            response = llm(prompt, system_prompt=system_prompt)

        st.write("Extracting locations from the response...")
        locations = extract_locations(response)

        if locations:
            st.write(f"Locations found: {', '.join(locations)}")
            st.write("Generating the map...")

            map_obj = generate_map(locations, draw_lines=draw_lines)
            if map_obj:
                # Store the map object in the session state
                st.session_state['map_data'] = map_obj
        else:
            st.error("No locations found in the prompt.")

    # Display the map if it exists in session state
    if st.session_state['map_data']:
        st_folium(st.session_state['map_data'], width=700, height=500)

if __name__ == "__main__":
    main()
