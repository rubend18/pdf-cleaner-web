# PDF a PPTX - NotebookLM Cleaner

Herramienta web minimalista para convertir documentos PDF a presentaciones de PowerPoint (`.pptx`).

Esta aplicación fue creada para solucionar un problema específico: limpiar las exportaciones de **NotebookLM**, colocando automáticamente un parche blanco sobre el logo/marca de agua en la esquina inferior derecha antes de generar la diapositiva.

## 🚀 Funcionalidad

- **Limpieza Automática:** Aplica un recuadro blanco en la posición exacta del logo de NotebookLM.
- **Conversión Directa:** Transforma cada página del PDF en una diapositiva de PowerPoint de alta calidad.
- **Interfaz Simple:** Sin configuraciones complejas. Subir, procesar y descargar.
- **Optimizado para Móvil:** Funciona perfectamente desde el navegador de tu celular usando Streamlit Cloud.

## 🛠️ Requisitos del Sistema

El proyecto utiliza las siguientes librerías de Python, definidas en `requirements.txt`:

- `streamlit`
- `pymupdf`
- `python-pptx`

---

## 📖 Guía de Despliegue Paso a Paso

Si deseas montar tu propia versión de esta web para usarla desde el celular, sigue estos pasos. La solución ideal es usar **Streamlit Cloud** porque es gratuito, ejecuta Python en la nube y se conecta directamente a GitHub.

### Paso 1: Preparación de Archivos
Asegúrate de tener listos los dos archivos principales del proyecto:
1.  **`requirements.txt`**: Debe contener las librerías necesarias (`streamlit`, `pymupdf`, `python-pptx`).
2.  **`app.py`**: El código principal de la aplicación.

### Paso 2: Subir a GitHub
1.  Crea una cuenta en GitHub.com si aún no tienes una.
2.  Crea un **Nuevo Repositorio** (puedes llamarlo, por ejemplo: `pdf-cleaner-web`).
3.  Sube los archivos `app.py` y `requirements.txt` a ese repositorio.

### Paso 3: Desplegar la Web (Gratis)
1.  Ingresa a [share.streamlit.io](https://share.streamlit.io).
2.  Inicia sesión con tu cuenta de GitHub.
3.  Haz clic en **"New App"** (o "Deploy an app").
4.  Selecciona el repositorio que creaste en el paso anterior (`pdf-cleaner-web`).
5.  En el campo **"Main file path"**, asegúrate de que diga `app.py`.
6.  Haz clic en **Deploy**.

### Resultado
En unos minutos, Streamlit te generará una URL única (del estilo `pdf-cleaner-web.streamlit.app`).
* Podrás entrar a esa URL directamente desde tu celular.
* Verás un botón grande para subir archivos desde tu galería o almacenamiento móvil.
* Al presionar "Procesar", la nube hará el trabajo y te permitirá descargar el PPTX limpio.

---

## 📄 Estructura del Proyecto

- `app.py`: Código lógico de la conversión y la interfaz.
- `requirements.txt`: Dependencias para el servidor.
- `README.md`: Documentación y manual de despliegue.
