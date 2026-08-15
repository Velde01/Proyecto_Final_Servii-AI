import streamlit as st
import requests
import json
import re

# Configuración visual de la página
st.set_page_config(
    page_title="Servii AI - Diagnóstico de Servicios del Hogar",
    page_icon="🛠️",
    layout="centered"
)

# Estilos CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 15px;
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 0.85rem;
        margin-top: 50px;
        border-top: 1px solid #E5E7EB;
        padding-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div class="main-header">
        <h1>🛠️ Servii AI</h1>
        <p>Marketplace Inteligente de Mantenimiento y Servicios del Hogar</p>
    </div>
""", unsafe_allow_html=True)

# SECCIÓN: CÓMO FUNCIONA
with st.expander("ℹ️ ¿Cómo funciona Servii AI? (Haz clic para ver detalles)", expanded=False):
    st.markdown("""
    * **1. Describe tu problema:** Escribe lo que ocurre en tu casa (ej: *'el calefón pierde agua por la válvula'*).
    * **2. Análisis Inteligente:** Nuestro motor de IA evalúa la falla, determina la especialidad requerida y estima el nivel de urgencia.
    * **3. Ficha Técnica Estructurada:** Obtendrás un diagnóstico preliminar con lista de posibles materiales, tiempo estimado y un resumen técnico listo para cotizar.
    * **4. Sin visitas a ciegas:** Tanto el usuario como el profesional tienen claridad sobre el trabajo a realizar desde el primer minuto.
    """)

# SIDEBAR: API KEY
with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key:", type="password")
    st.caption("Obtén tu clave gratuita en [Google AI Studio](https://aistudio.google.com/).")

# ENTRADA DEL USUARIO
st.subheader("📋 Ingresa los detalles de la avería")
user_input = st.text_area(
    "Describe lo que sucede con el mayor detalle posible:",
    placeholder="Ejemplo: El calefón eléctrico hace saltar la llave general a los 5 minutos de encenderse...",
    height=120
)

# BOTÓN DE ACCIÓN
if st.button("🚀 Generar Diagnóstico Técnico", type="primary"):
    clean_key = api_key.strip() if api_key else ""
    if not clean_key:
        st.error("⚠️ Por favor, ingresa tu Gemini API Key en el panel lateral.")
    elif not user_input.strip():
        st.warning("⚠️ Debes ingresar una descripción de la avería para analizar.")
    else:
        try:
            with st.spinner("Buscando modelo activo y procesando avería..."):
                # 1. Obtener la lista real de modelos disponibles para esta clave
                list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={clean_key}"
                list_res = requests.get(list_url)
                
                if list_res.status_code != 200:
                    raise Exception(f"Clave de API inválida o error de acceso: {list_res.text}")
                
                models_data = list_res.json().get("models", [])
                
                # Filtrar modelos que soporten generación y descartar versiones no disponibles
                available_models = [
                    m["name"] for m in models_data 
                    if "generateContent" in m.get("supportedGenerationMethods", [])
                    and "2.5" not in m["name"]
                ]
                
                if not available_models:
                    available_models = ["models/gemini-1.5-flash", "models/gemini-1.5-pro"]

                # 2. Prompt con salida dirigida (JSON)
                prompt_completo = f"""
Actúa como un Director Técnico experto en mantenimiento del hogar, sanitaria, electricidad y albañilería.
Analiza la siguiente avería y responde OBLIGATORIAMENTE con un único objeto JSON válido sin texto adicional.

AVERÍA:
"{user_input}"

ESQUEMA JSON OBLIGATORIO:
{{
    "categoria": "Sanitaria | Electricidad | Cerrajería | Climatización | Albañilería | Pintura | Otro",
    "diagnostico_preliminar": "Explicación clara y concisa de la falla",
    "nivel_urgencia": "Bajo | Medio | Alto | Crítico",
    "profesional_requerido": "Especialidad del técnico requerido",
    "materiales_probables": ["material 1", "material 2"],
    "tiempo_estimado_horas": "Tiempo estimado (ej: 1 a 2 horas)",
    "resumen_para_tecnico": "Resumen técnico formal listo para enviar al especialista"
}}
"""
                data = None
                headers = {"Content-Type": "application/json"}
                payload = {
                    "contents": [{"parts": [{"text": prompt_completo}]}],
                    "generationConfig": {"temperature": 0.2}
                }

                # 3. Probar secuencialmente hasta encontrar el modelo habilitado
                for m_full in available_models:
                    gen_url = f"https://generativelanguage.googleapis.com/v1beta/{m_full}:generateContent?key={clean_key}"
                    res = requests.post(gen_url, headers=headers, json=payload)
                    
                    if res.status_code == 200:
                        res_json = res.json()
                        texto = res_json['candidates'][0]['content']['parts'][0]['text']
                        match = re.search(r'\{.*\}', texto, re.DOTALL)
                        json_str = match.group(0) if match else texto
                        data = json.loads(json_str)
                        break

                if data is None:
                    raise Exception("No se pudo obtener respuesta válida de los modelos disponibles con esta API Key.")

                # RENDERIZADO VISUAL DEL REPORTE
                st.success("✅ Diagnóstico generado con éxito")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Rubro", data.get("categoria", "N/A"))
                with col2:
                    st.metric("Urgencia", data.get("nivel_urgencia", "Medio"))
                with col3:
                    st.metric("Tiempo Estimado", data.get("tiempo_estimado_horas", "N/A"))

                st.markdown("### 🔍 Diagnóstico Preliminar")
                st.info(data.get("diagnostico_preliminar", ""))

                st.markdown(f"**Especialista asignado:** `{data.get('profesional_requerido', 'General')}`")

                st.markdown("### 🧰 Materiales e Insumos Probables")
                materiales = data.get("materiales_probables", [])
                if materiales and isinstance(materiales, list):
                    for item in materiales:
                        st.markdown(f"- {item}")
                else:
                    st.write("A evaluar por el técnico en sitio.")

                st.markdown("### 📄 Ficha Técnica para el Profesional")
                st.text_area("Copia este resumen para enviar al técnico:", value=data.get("resumen_para_tecnico", ""), height=100)

        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")

# FOOTER
st.markdown("""
    <div class="footer">
        <p>Servii AI © 2026 - Proyecto Final de IA: Prompt Engineering para Developers 3.0 (Coderhouse)</p>
    </div>
""", unsafe_allow_html=True)