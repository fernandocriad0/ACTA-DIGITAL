import streamlit as st

st.set_page_config(page_title="Acta Digital", page_icon="📝")

st.title("📝 Acta Digital")
st.write("Genera fácilmente el acta de una reunión.")

with st.form("acta_form"):
    titulo = st.text_input("Título del acta")
    asistentes = st.text_area("Asistentes (uno por línea)")
    acuerdos = st.text_area("Acuerdos")
    fecha = st.date_input("Fecha de la reunión")
    enviado = st.form_submit_button("Generar acta")

if enviado:
    st.success("✅ Acta generada:")
    st.markdown(f"### {titulo}")
    st.markdown(f"**Fecha:** {fecha}")
    st.markdown("**Asistentes:**")
    st.markdown("- " + "\n- ".join([a.strip() for a in asistentes.splitlines() if a.strip()]))
    st.markdown("**Acuerdos:**")
    st.write(acuerdos)
