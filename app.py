import streamlit as st
st.image("data:image/jpeg;base64,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", caption="hello????")
import requests
import json
import base64
from langchain_community.llms import OpenAI
from openai import OpenAI as OpenAIClient

# Sidebar - OpenAI API Key Input
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Dropdown Menu for Navigation
selected_tab = st.selectbox(
    "Select a Feature:",
    [
        "💬 Chat", "🖼️ Vision", "🎨 Image Generation",
        "🔊 Audio Generation", "🎙 Speech to Text",
        "🛑 Moderation", "🧠 Reasoning", "🛠 Functions"
    ]
)

if selected_tab == "💬 Chat":
    st.title('🦜🔗 Quickstart App')

    def generate_response(input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))

    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')

        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)

elif selected_tab == "🖼️ Vision":
    st.title("🖼️ Vision AI")

    image_url = st.text_input("Enter an Image URL:",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg")

    if st.button("Analyze Image"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": [
                            {"type": "text", "text": "What's in this image?"},
                            {"type": "image_url", "image_url": {"url": image_url}}
                        ]}
                    ],
                    max_tokens=300,
                )

                if response and hasattr(response, "choices"):
                    st.image(image_url, caption="Analyzed Image", use_column_width=True)
                    st.success(response.choices[0].message.content)
                else:
                    st.error("Failed to generate response. Please check your API key or image URL.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

elif selected_tab == "🎨 Image Generation":
    st.title("🎨 AI Image Generation")

    prompt = st.text_area("Enter a prompt for the image:", "a white siamese cat")
    size = st.selectbox("Select Image Size:", ["1024x1024", "512x512", "256x256"])

    if st.button("Generate Image"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=size,
                    quality="standard",
                    n=1,
                )

                if response and hasattr(response, "data"):
                    image_url = response.data[0].url
                    st.image(image_url, caption="Generated Image", use_column_width=True)
                    st.success("✅ Image generated successfully!")
                else:
                    st.error("⚠ Failed to generate image. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

elif selected_tab == "🛠 Functions":
    st.title("🛠 AI Functions (Tool Calling)")

    st.markdown("""
    ### How Function Calling Works
    OpenAI's GPT-4o model can **call functions** to retrieve real-world data.  
    This example fetches the **temperature in both Celsius and Fahrenheit** along with a **weather description** using a weather API.
    """)

    # Function to get weather data from Open-Meteo API
    def get_weather(latitude, longitude):
        try:
            response = requests.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode&hourly=temperature_2m"
            )
            data = response.json()
            temp_c = data['current']['temperature_2m']
            temp_f = (temp_c * 9/5) + 32  # Convert Celsius to Fahrenheit
            weather_code = data['current']['weathercode']

            # Mapping weather codes to descriptions
            weather_descriptions = {
                0: "Clear sky ☀️",
                1: "Mainly clear 🌤",
                2: "Partly cloudy ⛅",
                3: "Overcast ☁️",
                45: "Fog 🌫",
                48: "Rime fog 🌫❄",
                51: "Light drizzle 🌦",
                53: "Moderate drizzle 🌦",
                55: "Heavy drizzle 🌧",
                61: "Light rain 🌦",
                63: "Moderate rain 🌧",
                65: "Heavy rain 🌧🌧",
                71: "Light snow 🌨",
                73: "Moderate snow 🌨🌨",
                75: "Heavy snow ❄️❄️❄️",
                95: "Thunderstorms ⛈",
                96: "Thunderstorms with light hail ⛈",
                99: "Thunderstorms with heavy hail 🌩",
            }

            weather_description = weather_descriptions.get(weather_code, "Unknown weather condition 🤷")
            return temp_c, temp_f, weather_description

        except Exception as e:
            return None, None, f"Error retrieving weather data: {str(e)}"

    # Expanded list of locations including Miami
    locations = {
        "Miami, USA": (25.7617, -80.1918),
        "New York, USA": (40.7128, -74.0060),
        "Los Angeles, USA": (34.0522, -118.2437),
        "Chicago, USA": (41.8781, -87.6298),
        "Houston, USA": (29.7604, -95.3698),
        "Toronto, Canada": (43.6532, -79.3832),
        "Vancouver, Canada": (49.2827, -123.1207),
        "Buenos Aires, Argentina": (-34.6037, -58.3816),
        "São Paulo, Brazil": (-23.5505, -46.6333),
        "Mexico City, Mexico": (19.4326, -99.1332),
        "Lima, Peru": (-12.0464, -77.0428),
        "Bogotá, Colombia": (4.7110, -74.0721),
        "Santiago, Chile": (-33.4489, -70.6693)
    }

    # User selection method (dropdown or manual entry)
    input_method = st.radio("Choose input method:", ["Select a City", "Enter Latitude/Longitude"])

    if input_method == "Select a City":
        location_name = st.selectbox("Select a location:", list(locations.keys()))
        latitude, longitude = locations[location_name]
    else:
        latitude = st.number_input("Enter Latitude:")
        longitude = st.number_input("Enter Longitude:")

    if st.button("Get Weather via Function Call"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                temp_c, temp_f, weather_description = get_weather(latitude, longitude)

                if temp_c is not None:
                    st.success(f"✅ Weather Retrieved for {location_name if input_method == 'Select a City' else 'your custom location'}")
                    st.write(f"🌡 **Temperature:** {temp_c:.1f}°C / {temp_f:.1f}°F")
                    st.write(f"🌦 **Conditions:** {weather_description}")
                else:
                    st.error("⚠ Failed to retrieve weather data. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")



elif selected_tab == "🧠 Reasoning":
    st.title("🧠 AI Reasoning")

    st.markdown("""
    ### How Reasoning Works
    The **O1 model** introduces **reasoning tokens**.  
    These tokens allow the model to **"think"** before providing a final response.
    """)

    reasoning_prompt = st.text_area("Enter a problem to solve:",
        "Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.")

    if st.button("Generate Reasoned Response"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="o1",
                    messages=[{"role": "user", "content": reasoning_prompt}]
                )

                if response and hasattr(response, "choices"):
                    st.success("✅ Reasoning Completed!")
                    st.write(response.choices[0].message.content)
                else:
                    st.error("⚠ Failed to generate reasoning response. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")
