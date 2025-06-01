import streamlit as st
import base64

# ✅ Must be first Streamlit command
st.set_page_config(page_title="Coca-Cola Campaign Explorer", layout="centered")


# Function to convert local image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def set_bg_from_local(image_path):
    encoded = get_base64_image(image_path)
    css = f"""
    <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: white;
        }}
        .css-1d391kg, .stButton>button {{
            background-color: white;
            color: black;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ✅ Set background image from local file
set_bg_from_local("images/bg.jpg")

# --- Your Coca-Cola campaign content starts here ---
st.title("🥤 Coca-Cola Campaign Explorer")
st.write("Explore iconic Coca-Cola marketing campaigns and decode their brand strategy!")

campaigns = {
    "Share a Coke": {
        "year": 2011,
        "image": "images/shareacoke.png",
        "description": "Launched in Australia, this campaign replaced the logo with first names, encouraging personal sharing.",
        "why_iconic": [
            "Boosted sales by 7% in Australia and reversed a decade-long decline in the US.",
            "250 million bottles sold in Australia; global rollout across 80 countries.",
            "Generated 1+ billion social media impressions and 500K Instagram photos."
        ],
        "key_takeaway": ["Make it personal, and people will share."],
        "target_audience": "Global youth and millennials"
    },

    "Holidays are Coming": {
        "year": 1995,
        "image": "images/holiday.png",
        "description": "Introduced the iconic Coca-Cola Christmas truck, lighting up festive cheer every year.",
        "why_iconic": [
            "25% increase in sales during holidays.",
            "Became a nostalgic symbol tied to the Christmas spirit.",
            "Scored a perfect 5.9 on System1’s ad testing tool in 2023."
        ],
        "key_takeaway": ["Consistency builds festive brand magic."],
        "target_audience": "Families and holiday shoppers"
    },

    "Thanda Matlab Coca-Cola": {
        "year": 2003,
        "image": "images/thanda.png",
        "description": "Connected Coca-Cola with Indian culture through a catchy line meaning 'cold means Coca-Cola'.",
        "why_iconic": [
            "37% growth in rural markets vs. 24% in urban",
"Rural penetration tripled from 9% (2001) to 25% (2003).",
"35% of total Coke sales in India came from rural areas post-campaign"
        ],
        "key_takeaway": ["Speak the local language, own the market."],
        "target_audience": "Indian youth and rural markets"
    },

    "Coke Studio": {
        "year": 2008,
        "image": "images/cokestudio.jpeg",
        "description": "A musical fusion platform promoting cultural harmony through traditional and modern sounds.",
        "why_iconic": [
            "Created strong emotional brand resonance.",
            "Expanded Coke's appeal across South Asia.",
            "Set a benchmark in content-driven marketing."
        ],
        "key_takeaway": ["Let music tell your brand story."],
        "target_audience": "Millennials and music lovers"
    },

    "Coca-Cola Mantra Challenge": {
        "year": 2025,
        "image": "images/mantra.jpeg",
        "description": "A live business challenge for MBA/PGDM students to solve real-world brand problems.",
        "why_iconic": [
            "Engaged 20,000+ students across India.",
            "Winners received internships with ₹2.5L/month stipend.",
            "Strengthened employer brand in top B-schools."
        ],
        "key_takeaway": ["Empower youth, amplify innovation."],
        "target_audience": "MBA/PGDM students in India"
    }

}

option = st.selectbox("Select a Campaign", list(campaigns.keys()))
show = st.button("Show Campaign Info")


if show:
    campaign = campaigns[option]
    st.markdown(f"**Year:** {campaign['year']}")
    st.markdown(f"**Target Audience:** {campaign['target_audience']}")
    st.image(campaign["image"], width=400)
    st.markdown(f"### About {option}")
    st.write(campaign["description"])
    st.markdown("### Why was it iconic?")
    for point in campaign["why_iconic"]:
        st.write(f"- {point}")
    st.markdown("### Key Takeaways")
    for takeaway in campaign["key_takeaway"]:
        st.write(f"- {takeaway}")
    st.success("This is how Coca-Cola crafted emotional and viral brand stories!")

st.markdown("---")
st.caption("Built by a coder-turned-MBA, inspired by #CokeAmbassador #unstop #TheCocaColaMantraChallenge2025.")
