import random
import streamlit as st
from PIL import Image, ImageDraw
import requests
#from pydub import AudioSegment
#from IPython.display import Audio
import io
def main():
    set_page_config()


    st.title("👍👍")

    image_link = "https://drive.google.com/uc?export=view&id=1AV2QKF_4ktL6FZO3bH-_tHZDz5IurfQA"

    image = Image.open(requests.get(image_link, stream=True).raw)
    st.image(image, use_column_width=True)
    st.markdown("<p style='font-size: 14px;'>(Remember to click the play button after clicking the celebrate button!!)</p>", unsafe_allow_html=True)

    
    if st.button("Celebrate!!!!!", key="birthday_button", help="Then, click on the play button!"):
        for _ in range(4):
            st.balloons()
        audio_link = "https://drive.google.com/uc?export=view&id=1A_r-_Xd3eOUsKwTZXpO04BfmvpLEIgPW"

        st.audio(audio_link, format="audio/mp3")
        st.markdown("<h1 style='text-align: center; color: #FF69B4;'>Happy Birthday!!!!!!!!!</h1>", unsafe_allow_html=True)

        generate_confetti_animation()
        st.markdown("<div style='text-align: center;'><p style='font-size: 24px;'>Wishing you a day filled with joy and laughter!!!!!!✨🌟</p></div>",
            unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'><p style='font-size: 24px;'>May this year be filled with success and exciting new ""branch"" adventures, Topper!!!!! 🎉🎈</p></div>",
            unsafe_allow_html=True)




def set_page_config():
    page_bg_color = "dark blue"
    page_fg_color = "#f8f9fa"
    page_css = f"""
        <style>
        .stApp {{
            background-color: {page_bg_color};
            color: {page_fg_color};
        }}
        </style>
    """
    st.markdown(page_css, unsafe_allow_html=True)

def generate_confetti_animation():
    canvas_width = 800
    canvas_height = 400
    num_confetti = 300

    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    random.seed(42)
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 215, 0),  # Gold
        (128, 0, 128),  # Purple
        (255, 165, 0),  # Orange
    ]
    confetti_size_range = (5, 20)
    velocity_range = (1, 5)
    angular_velocity_range = (-5, 5)

    for _ in range(num_confetti):
        confetti_size = random.randint(*confetti_size_range)
        confetti_color = random.choice(colors)
        confetti_x = random.randint(0, canvas_width)
        confetti_y = random.randint(0, canvas_height)
        velocity_x = random.uniform(*velocity_range)
        velocity_y = random.uniform(*velocity_range)
        angular_velocity = random.uniform(*angular_velocity_range)

        for _ in range(confetti_size):
            draw.rectangle([(confetti_x, confetti_y), (confetti_x + 1, confetti_y + 1)], fill=confetti_color)
            confetti_x += velocity_x
            confetti_y += velocity_y
            velocity_y += 0.1
            velocity_x *= 0.98
            angular_velocity *= 0.95

            confetti_y = min(confetti_y, canvas_height - 1)

            if confetti_x < 0 or confetti_x >= canvas_width or confetti_y >= canvas_height - 1:
                break

    st.image(canvas, use_column_width=True)
    #pass

if __name__ == '__main__':
    main()
