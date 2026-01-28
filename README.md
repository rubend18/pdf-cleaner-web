# PDF a PPTX - NotebookLM Cleaner

Herramienta web minimalista para convertir documentos PDF a presentaciones de PowerPoint (`.pptx`).

Esta aplicación fue creada para solucionar un problema específico: limpiar las exportaciones de **NotebookLM**, colocando automáticamente un parche blanco sobre el logo/marca de agua en la esquina inferior derecha antes de generar la diapositiva.

## 🚀 Funcionalidad

- **Limpieza Automática:** Aplica un recuadro blanco en la posición exacta del logo de NotebookLM.
- **Conversión Directa:** Transforma cada página del PDF en una diapositiva de PowerPoint de alta calidad.
- **Interfaz Simple:** Sin configuraciones complejas. Subir, procesar y descargar.
- **Optiminzado para Móvil:** Funciona perfectamente desde el navegador de tu celular usando Streamlit Cloud.

## 🛠️ Requisitos

El proyecto utiliza las siguientes librerías de Python (asegúrate de tenerlas en tu `requirements.txt`):

- `streamlit`
- `pymupdf`
- `python-pptx`

## 📦 Cómo usarlo

### En la Nube (Recomendado para Celular)
1. Sube este código (`app.py` y `requirements.txt`) a un repositorio de GitHub.
2. Conecta tu cuenta en [Streamlit Cloud](https://share.streamlit.io).
3. Despliega la app seleccionando tu repositorio.

### En Local (PC)
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
