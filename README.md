# 🛠️ Servii AI - Diagnóstico Inteligente de Servicios del Hogar

**Proyecto Final - IA: Prompt Engineering para Developers 3.0** *Coderhouse*

---

## 📌 Descripción del Proyecto

**Servii AI** es una aplicación web interactiva desarrollada con **Streamlit** e impulsada por los modelos fundacionales de **Google Gemini**. Su objetivo principal es resolver la asimetría de información en el mercado de reparaciones y mantenimiento doméstico (sanitaria, electricidad, cerrajería, albañilería, climatización, etc.).

A través de un **System Prompt con salida dirigida (Structured Output)**, la aplicación analiza descripciones en lenguaje natural ingresadas por los usuarios y genera automáticamente una **Ficha Técnica Estructurada en formato JSON**, permitiendo presupuestar reparaciones con precisión y eliminando visitas técnicas preliminares a ciegas.

---

## 🚀 Características Principales

- **Diagnóstico Preliminar Inmediato:** Traduce descripciones cotidianas en fallas técnicas específicas.
- **Categorización y Clasificación de Urgencia:** Asigna el rubro adecuado y clasifica la criticidad del problema (Bajo, Medio, Alto, Crítico).
- **Estimación de Insumos y Tiempos:** Sugiere materiales probables y calcula el rango horario necesario para la intervención.
- **Ficha Técnica Profesional:** Entrega un resumen listo para copiar y enviar al especialista asignado.
- **Salida Dirigida Estricta (JSON):** Respuestas consistentes, sin alucinaciones de formato, parseadas dinámicamente en componentes nativos de Streamlit.
- **Conexión REST Resiliente:** Búsqueda y conexión dinámica con los modelos activos de la API de Google Gemini.

---

## 🧠 Arquitectura de Prompting y Salida Dirigida

La aplicación implementa técnicas avanzadas de **Prompt Engineering**:
1. **Asignación de Rol de Experto:** Director Técnico especializado en mantenimiento integral.
2. **Restricciones Negativas:** Prohibición estricta de texto introductorio, bloques de código markdown o información no verificable.
3. **Esquema JSON Estricto:**

```json
{
  "categoria": "Sanitaria | Electricidad | Cerrajería | Climatización | Albañilería | Pintura | Otro",
  "diagnostico_preliminar": "Explicación clara y concisa de la falla",
  "nivel_urgencia": "Bajo | Medio | Alto | Crítico",
  "profesional_requerido": "Especialidad del técnico requerido",
  "materiales_probables": ["material 1", "material 2"],
  "tiempo_estimado_horas": "Tiempo estimado (ej: 1 a 2 horas)",
  "resumen_para_tecnico": "Resumen técnico formal listo para enviar al especialista"
}