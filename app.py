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
   
import streamlit as st
import hashlib, time, json
st.title("Acta Digital — Import Test")

st.write("✅ Librerías importadas:")
st.code("streamlit, hashlib, time, json")

text = st.text_input("Texto a hashear (SHA-256):", "hola mundo")
if text:
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    st.write("Hash:", sha)

st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))

