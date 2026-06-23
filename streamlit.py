import streamlit as st

# st.title('MyAPP')
# st.write('Hello world')

# st.header('Main Title')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> text element

# st.title("Main Title")
# st.header("Header")
# st.subheader("Sub Header")
# st.text("Simple Text")
# st.markdown("**Bold Text**")
# st.success("Success Message")
# st.error("Error Message")
# st.warning("Warning Message")
# st.info("Info Message")


# user input

# text input

name = st.text_input("Enter Name")

if name:
    st.write("Hello", name)
    
    
# number input

age = st.number_input("Enter Age")
st.write(age)

# button

if st.button("Click Me"):
    st.write("Button Clicked")
    
    
# widget

# select box

city = st.selectbox(
    "Select City",
    ["Nagpur","Pune","Mumbai"]
)

st.write(city)


# radio button

gender = st.radio(
    "Gender",
    ["Male","Female"]
)

st.write(gender)


# check box


if st.checkbox("Show Data"):
    st.write("Data Visible")
    
    
    
# slider


salary = st.slider(
    "Salary",
    10000,
    100000,
    25000
)

st.write(salary)



# dataframe

import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C"],
    "Marks":[80,90,70]
})

st.dataframe(df)


# file upload


file = st.file_uploader("Upload CSV")

if file:
    import pandas as pd
    df = pd.read_csv(file)
    st.dataframe(df)
    
    
# image

from PIL import Image
import streamlit as st

img = Image.open("cat.png")
st.image(img)

# graph

import streamlit as st
import pandas as pd

data = {
    "Year":[2021,2022,2023],
    "Sales":[100,150,200]
}

df = pd.DataFrame(data)

st.line_chart(df.set_index("Year"))

