import streamlit as st
import fitz  # PyMuPDF
from pptx import Presentation
from pptx.util import Pt
import io
import os

# Configuración de la página
st.set_page_config(page_title="PDF a PPTX", layout="centered")

st.title("📄 PDF a PPTX")
st.write("Sube tu PDF para tapar el logo de NotebookLM y convertirlo a PowerPoint.")

# Widget para subir archivo
uploaded_file = st.file_uploader("Sube tu PDF aquí", type=["pdf"])

def procesar_pdf(file_stream):
    # Abrir PDF desde la memoria
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    prs = Presentation()

    # --- CONFIGURACIÓN DEL RECUADRO ---
    ancho_box = 97
    alto_box = 12
    margen_inf = 9
    margen_der = 10

    # Barra de progreso
    progress_bar = st.progress(0)
    total_pages = len(doc)

    for i, page in enumerate(doc):
        w_page = page.rect.width
        h_page = page.rect.height

        # Dibujar parche blanco
        rect = fitz.Rect(
            w_page - margen_der - ancho_box,
            h_page - margen_inf - alto_box,
            w_page - margen_der,
            h_page - margen_inf
        )
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

        # Renderizar página a imagen en memoria (sin guardar en disco)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_bytes = pix.tobytes("png")
        image_stream = io.BytesIO(img_bytes)

        # Crear slide PPT
        prs.slide_width = Pt(w_page)
        prs.slide_height = Pt(h_page)
        blank_layout = prs.slide_layouts[6] 
        slide = prs.slides.add_slide(blank_layout)
        
        # Insertar imagen desde memoria
        slide.shapes.add_picture(image_stream, 0, 0, width=prs.slide_width, height=prs.slide_height)

        # Actualizar barra
        progress_bar.progress((i + 1) / total_pages)

    # Guardar PPTX en memoria
    pptx_out = io.BytesIO()
    prs.save(pptx_out)
    pptx_out.seek(0)
    return pptx_out

if uploaded_file is not None:
    if st.button("Procesar y Convertir"):
        with st.spinner("Procesando páginas..."):
            try:
                # Procesamos el archivo
                resultado_pptx = procesar_pdf(uploaded_file)
                
                st.success("¡Conversión completada!")
                
                # Botón de descarga
                st.download_button(
                    label="📥 Descargar PPTX",
                    data=resultado_pptx,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}_limpio.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")