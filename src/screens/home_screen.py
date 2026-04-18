import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_base_layout()
    style_background_home()

    # Header
    header_home()

    # Layout
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://images.openai.com/static-rsc-4/YeDghE2j8CabFflAFp78fbCL_30NoN7bj9FTuDAzk5hJZ0SEHZE8M6g7TShkA7hOg4m5r6FuhcGRWZXBxcMN6JT_F4Ckj6Unk5pWJQ8zQ4bw-_TPCz650gK6g8uKbz_aQFZNjqDW70Fikl-VhtSv32CgOntWy3pzpGyPi2Fa1XwQPKOZl-8VIRKnWqmfaeC2?purpose=fullsize" , width=120)

        if st.button("Student Portal ↗️", key="student", type="primary"):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://images.openai.com/static-rsc-4/esKe900UAL55F-VZKwXuRmrW5Dv8FosSk1vICglnqm23IU8_ygpRnULaIk9qQRFk0EqZmwNQektHNFon56KGScgAdVZr5eSPDW8weL8z36IGyqJC2Hmku_oP7hv3zMlc2Uf9BtjttdR9HEYhpds4I54wAbtCKiCzYTFuKXWMimw7wr8GceuAP-ktyTHZRMKJ?purpose=fullsize" , width=120)

        if st.button("Teacher Portal ↗️ ", key="teacher", type="primary"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()