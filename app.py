import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="🎨 Tablero Pro",
    page_icon="🎨",
    layout="wide"
)

# ---------------- CSS PERSONALIZADO ----------------
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Título */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
}

/* Animación */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Tarjeta del canvas */
.canvas-container {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
    text-align: center;
}

/* Sidebar */
.css-1d391kg {
    background-color: #111 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITULO ----------------
st.markdown('<div class="title">🎨 Tablero de Dibujo Interactivo</div>', unsafe_allow_html=True)
st.write("")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Configuración")

    st.subheader("📐 Dimensiones")
    canvas_width = st.slider("Ancho", 300, 800, 600, 50)
    canvas_height = st.slider("Alto", 200, 600, 400, 50)

    st.subheader("🖌️ Herramientas")
    drawing_mode = st.selectbox(
        "Modo de dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider("Grosor", 1, 30, 10)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

# ---------------- CANVAS CENTRADO ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="canvas-container">', unsafe_allow_html=True)

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FEEDBACK ----------------
if canvas_result.json_data is not None:
    st.success("✅ Dibujo actualizado en tiempo real")
