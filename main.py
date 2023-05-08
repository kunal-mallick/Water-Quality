import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline

st.set_page_config(layout="wide")

load = open('model.pkl','rb')
model = pickle.load(load)

# Headder
def Headder():

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://raw.githubusercontent.com/kunal-mallick/Kaggle-Project/main/Water%20Quality(Drinking%20Water%20Potability)/img/Header.png");
        background-size: 100%;
        background-position: top;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Body
def body():

    # Pading
    st.text('')
    st.text('')
    st.text('')

    ## Body(title)
    st.markdown("""
    <style>
    .big-font {
    font-size:48px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Is The Water At Your Home Safe For Drinking?</p>', unsafe_allow_html=True)

    ## Body(img)
    img = st.columns(5)
    img[1].markdown('<img src ="https://domf5oio6qrcr.cloudfront.net/medialibrary/7909/b8a1309a-ba53-48c7-bca3-9c36aab2338a.jpg" ></img>', unsafe_allow_html=True)

    ## Body(text)
    st.markdown("""
    <style>
    .big-font {
    font-size:18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p>Drinking water is a vital resource for human health and well-being. It is essential for staying hydrated, maintaining bodily functions, and preventing dehydration. Access to clean and safe drinking water is a basic human right, yet many people around the world do not have access to it. Contaminated water can cause waterborne diseases, such as cholera and dysentery, which can be deadly, particularly for children and those with weakened immune systems. Ensuring that everyone has access to clean drinking water is crucial for public health and a fundamental responsibility of governments worldwide.</p>', unsafe_allow_html=True)

    st.markdown('<p>Water is the most abundant substance on Earth, covering about 71% of its surface. However, only about 2.5% of this water is fresh water, and most of it is frozen in glaciers and ice caps. The remaining fresh water is found in rivers, lakes, groundwater, and the atmosphere. The availability and quality of fresh water vary greatly depending on geographic location, climate, and human activities. Some regions have abundant fresh water resources, while others face water scarcity and stress. Water scarcity occurs when the demand for water exceeds the available supply, or when the quality of water is too poor to meet the needs of the population. Water stress occurs when the available water resources are insufficient to satisfy the long-term average requirements of the population.</p>', unsafe_allow_html=True)

    st.markdown('<p>According to the World Health Organization (WHO), about 2.2 billion people lack access to safely managed drinking water services, meaning that they do not have a reliable source of water that is free from contamination and available when needed. About 785 million people lack even a basic drinking water service, meaning that they have to collect water from unprotected wells or surface water sources. These people are mainly located in sub-Saharan Africa and Asia. Moreover, about 1.8 billion people use a source of drinking water that may be contaminated with fecal matter, exposing them to the risk of waterborne diseases. The WHO estimates that about 485 000 deaths per year are caused by diarrheal diseases linked to unsafe drinking water.</p>', unsafe_allow_html=True)

    st.markdown('<p>Access to clean and safe drinking water is a basic human right that is essential for human dignity and survival. It is also a prerequisite for achieving other human rights, such as the right to health, education, food, and work. Water is necessary for sustaining life, health, hygiene, sanitation, agriculture, industry, and ecosystems. Without adequate access to water, people may suffer from thirst, hunger, disease, poverty, and conflict. Therefore, ensuring that everyone has access to clean drinking water is crucial for public health and a fundamental responsibility of governments worldwide.</p>', unsafe_allow_html=True)

    st.markdown('<p>Governments have the primary duty to respect, protect, and fulfill the human right to water for their citizens. This means that they have to ensure that everyone has sufficient, safe, acceptable, physically accessible, and affordable water for personal and domestic use. They also have to prevent and eliminate any discrimination or inequality in accessing water services or resources. They have to adopt appropriate laws, policies, regulations, and institutions to manage and allocate water resources effectively and sustainably. They have to monitor and report on the status of water services and resources in their countries. They have to cooperate with other countries and international organizations to address transboundary and global water issues.</p>', unsafe_allow_html=True)

    st.markdown('<p>However, governments alone cannot ensure universal access to clean drinking water. They need the support and participation of various stakeholders, such as civil society organizations, private sector entities,</p>', unsafe_allow_html=True)


# Prediction
def pred(PH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_Carbon, Trihalomethanes, Turbidity):

    sc = StandardScaler()
    xtest = sc.fit_transform([[PH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_Carbon, Trihalomethanes, Turbidity]])
    prediction = model.predict(xtest)
    return prediction

# Water Checker
def Water_Checker():
    ## Water Checker(title)
    st.image('https://raw.githubusercontent.com/kunal-mallick/Kaggle-Project/main/Water%20Quality(Drinking%20Water%20Potability)/img/Frame%201.png')

    ## Water Checker(input)
    c1 = st.columns(3)
    c2 = st.columns(3)
    c3 = st.columns(3)


    PH = c1[0].slider('PH Value', 0, 14)
    Hardness = c1[1].slider('Hardness Value', 47, 323)
    Solids = c1[2].slider('Solids Value', 323, 61227)


    Chloramines = c2[0].slider('Chloramines Value', 1, 13)
    Sulfate =  c2[1].slider('Sulfate Value', 129, 481)
    Conductivity = c2[2].slider('Conductivity Value', 181, 753)

    Organic_Carbon = c3[0].slider('Organic Carbon Value', 2, 28)
    Trihalomethanes = c3[1].slider('Trihalomethanes Value', 0, 124)
    Turbidity = c3[2].slider('Turbidity Value', 1, 6)

    if st.button('Predict'):

        result = pred(PH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_Carbon, Trihalomethanes, Turbidity)
        if (result == 1):
            st.success('Water is safe for human consumption')

        else:
            st.error('Water is not safe for human consumption', )

# Main

def main():
    Headder()
    body()
    Water_Checker()


if __name__ == '__main__':

    main()    

## Footer

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<img src ='https://raw.githubusercontent.com/kunal-mallick/Kaggle-Project/main/Water%20Quality(Drinking%20Water%20Potability)/img/Frame%202.png' style="vertical-align:centre"></img>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)
