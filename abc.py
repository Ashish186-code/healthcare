import streamlit as st

def home_page():
    st.markdown("<h1 style='text-align: center; font-size: 50px;color: yellow;'>HealthCare Guidance</h1>", unsafe_allow_html=True)
    selected_option = st.selectbox("Select an option", ["Diseases", "Drugs", "Variants", "Genes"])
    page_bg_img = '''
        <style>
        body {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM0bdgiorxP3EY7paJ6e8d99pYTCOXdPrYRA&usqp=CAU");
            background-size: cover;
        }
        </style>
        '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    if st.button("Submit"):
        st.session_state["selected_option"] = selected_option
        st.session_state["page"] = "About"

def about_page():
    columns = st.columns(4)
    Diseases=["abc","def","kbc"]
    Drugs=["abc","def","kbc"]
    Variants=["abc","def","kbc"]
    Genes=["abc","def","kbc"]
    st.write(f"You have selected the option: {st.session_state['selected_option']}")
       
    with columns[0]:
        st.header("Diseases")
        st.write(Diseases)
    
    with columns[1]:
        st.header("Drugs")
        st.write(Drugs)
    
    with columns[2]:
        st.header("Variants")
        st.write(Variants)
    
    with columns[3]:
        st.header("Genes")
        st.write(Genes)

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    if st.session_state["page"] == "Home":
        home_page()
    elif st.session_state["page"] == "About":
        about_page()

if __name__ == "__main__":
    main()
