import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

def main():
    if 'login_type' not in st.session_state:
        params = st.query_params
        url_role = params.get("role", None)
        if url_role in ['teacher', 'student']:
            st.session_state['login_type'] = url_role
        else:
            st.session_state['login_type'] = None

    if st.session_state['login_type']:
        st.query_params["role"] = st.session_state['login_type']
    else:
        st.query_params.clear()

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

if __name__ == "__main__":
    main()