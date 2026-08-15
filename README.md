PROYECTO FINAL: IA - PROMPT ENGINEERING PARA DEVELOPERS 3.0

1. PORTADA Y DATOS GENERALES
- Proyecto: Servii AI
- Alumno: [Tu Nombre y Apellido]
- Comisión: [Tu Número de Comisión]
- Repositorio GitHub: [PEGÁ ACÁ EL LINK DE TU REPO]
- App Desplegada en Streamlit: [PEGÁ ACÁ EL LINK DE STREAMLIT CLOUD]

2. PROBLEMÁTICA
En Uruguay y la región, la contratación de servicios de mantenimiento del hogar (sanitaria, electricidad, cerrajería) sufre de alta fricción e incertidumbre. Los usuarios no tienen conocimientos técnicos para diagnosticar averías y los profesionales pierden tiempo valioso en visitas de evaluación no remuneradas.

3. SOLUCIÓN PROPUESTA
Servii AI actúa como un Director Técnico Virtual que traduce descripciones informales o imágenes de usuarios en Fichas Técnicas estandarizadas, permitiendo diagnósticos inmediatos y presupuestos certeros sin visitas a ciegas.

4. ARQUITECTURA TÉCNICA Y SALIDA DIRIGIDA
- Framework Frontend: Streamlit.
- Modelo Fundacional: Google Gemini 1.5 Flash.
- Tipo de Prompting: System Prompt con Salida Dirigida (Structured Output) forzando formato JSON estricto mediante response_mime_type="application/json".
- Esquema JSON Generado: categoria, diagnostico_preliminar, nivel_urgencia, profesional_requerido, materiales_probables, tiempo_estimado_horas y resumen_para_tecnico.

5. FACTIBILIDAD ECONÓMICA
- Costo por consulta: ~$0.0005 USD (Gemini Flash).
- Viabilidad: Alta rentabilidad con costos de procesamiento marginales frente a comisiones de servicio del 10%-15%.