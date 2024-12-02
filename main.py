#===============================================
# This web program by Maria Luznedy, Hugo Fernando
# Nov 28/2024
# ver:1
# for: Hospitality.com
#=======================================================

import streamlit as st
from PIL import Image # import Image from pillow to open images
from forms.contact import contact_form

img=Image.open("img\\brandmark-design.png")
st.logo(img)

@st.dialog("Contact Me")

def show_contact_form():
    contact_form()

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

st.set_page_config(page_title="Distinct", layout="wide")

about_page =st.Page(
    page="pages/about.py",
    title="Home",
    #icon="img/person.png",
    icon=":material/home:"
)
admin_page=st.Page(
    page="pages/admin.py",
    title="Admin",
    icon=":material/admin_meds:",
    default=True,
)
dash_page=st.Page(
    page="pages/dash.py",
    title="Dash",
    #icon="img/person.png",
    icon=":material/bar_chart:"
)
data_page=st.Page(
    page="pages/data.py",
    title="More Data",
    #icon="img/person.png",
    icon=":material/docs:"
)
eval_page=st.Page(
    page="pages/eval.py",
    title="Eval",
    #icon="img/person.png",
    icon=":material/quiz:"
)
pay_page=st.Page(
    page="pages/pay.py",
    title="Pay",
    #icon="img/person.png",
    icon=":material/shopping_cart:"
)
train_page=st.Page(
    page="pages/training.py",
    title="Training",
    #icon="img/person.png",
    icon=":material/person:"
)

chatbot_page =st.Page(
    page="pages/chatbot.py",
    title="ChatBot",
    #icon="img/person.png",
    icon=":material/smart_toy:"
)


#-----NAVIGATION SETUP [WITHOUT SECTIONS]----

#pg=st.navigation(pages=[admin_page,dash_page,data_page,eval_page,pay_page,train_page])
pg = st.navigation(
    {
        "Home": [about_page],
        "Menu": [admin_page,data_page,eval_page,pay_page,train_page,dash_page,chatbot_page],

    }
)

#st.sidebar.image(img, width=150)

#----- RUN NAvIGATION---------
pg.run()

def main(mess):
    # Use a breakpoint in the code line below to debug your script.
    #st.sidebar.header("Menu")
    st.title(mess)  # Press Ctrl+F8 to toggle the breakpoint.
    # --- SHARED ON ALL PAGES ---

    #st.sidebar.button("Login", type="primary", use_container_width=True)
    #st.sidebar.write("")
    #st.sidebar.write("")
    #st.sidebar.markdown("##### Contact Us")
    #st.sidebar.markdown("Made with ❤️ by [Distinct](https://youtube.com/@DistinctT.R.A.I.N.-ing)")
    #if st.sidebar.button("✉️ Contact Me"):
    #    show_contact_form()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #st.sidebar.image(img, width=250)
    main('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
