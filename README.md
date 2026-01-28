# PDF a PPTX - NotebookLM Cleaner

Herramienta web minimalista para convertir documentos PDF a presentaciones de PowerPoint (`.pptx`).

Esta aplicación fue creada para solucionar un problema específico: limpiar las exportaciones de **NotebookLM**, colocando automáticamente un parche blanco sobre el logo/marca de agua en la esquina inferior derecha antes de generar la diapositiva.

## 🚀 Funcionalidad

- **Limpieza Automática:** Aplica un recuadro blanco en la posición exacta del logo de NotebookLM.
- **Conversión Directa:** Transforma cada página del PDF en una diapositiva de PowerPoint de alta calidad.
- **Interfaz Simple:** Sin configuraciones complejas. Subir, procesar y descargar.
- [cite_start]**Optimizado para Móvil:** Funciona perfectamente desde el navegador de tu celular usando Streamlit Cloud[cite: 10, 11].

## 🛠️ Requisitos del Sistema

[cite_start]El proyecto utiliza las siguientes librerías de Python, definidas en `requirements.txt`[cite: 4, 5]:

- `streamlit`
- `pymupdf`
- `python-pptx`

---

## 📖 Guía de Despliegue Paso a Paso

Si deseas montar tu propia versión de esta web para usarla desde el celular, sigue estos pasos. [cite_start]La solución ideal es usar **Streamlit Cloud** porque es gratuito, ejecuta Python en la nube y se conecta directamente a GitHub[cite: 2, 3].

### Paso 1: Preparación de Archivos
[cite_start]Asegúrate de tener listos los dos archivos principales del proyecto[cite: 4]:
1.  [cite_start]**`requirements.txt`**: Debe contener las librerías necesarias (`streamlit`, `pymupdf`, `python-pptx`)[cite: 4, 5].
2.  **`app.py`**: El código principal de la aplicación.

### Paso 2: Subir a GitHub
1.  [cite_start]Crea una cuenta en GitHub.com si aún no tienes una[cite: 6].
2.  [cite_start]Crea un **Nuevo Repositorio** (puedes llamarlo, por ejemplo: `pdf-cleaner-web`)[cite: 6].
3.  [cite_start]Sube los archivos `app.py` y `requirements.txt` a ese repositorio[cite: 6].

### Paso 3: Desplegar la Web (Gratis)
1.  [cite_start]Ingresa a [share.streamlit.io](https://share.streamlit.io)[cite: 7].
2.  [cite_start]Inicia sesión con tu cuenta de GitHub[cite: 7].
3.  [cite_start]Haz clic en **"New App"** (o "Deploy an app")[cite: 8].
4.  [cite_start]Selecciona el repositorio que creaste en el paso anterior (`pdf-cleaner-web`)[cite: 8].
5.  [cite_start]En el campo **"Main file path"**, asegúrate de que diga `app.py`[cite: 9].
6.  [cite_start]Haz clic en **Deploy**[cite: 9].

### Resultado
[cite_start]En unos minutos, Streamlit te generará una URL única (del estilo `pdf-cleaner-web.streamlit.app`)[cite: 10].
* [cite_start]Podrás entrar a esa URL directamente desde tu celular[cite: 10].
* [cite_start]Verás un botón grande para subir archivos desde tu galería o almacenamiento móvil[cite: 11].
* [cite_start]Al presionar "Procesar", la nube hará el trabajo y te permitirá descargar el PPTX limpio[cite: 12].

---

## 📄 Estructura del Proyecto

- `app.py`: Código lógico de la conversión y la interfaz.
- `requirements.txt`: Dependencias para el servidor.
- `README.md`: Documentación y manual de despliegue.
