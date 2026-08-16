# 🛠️ Servii AI - Marketplace Inteligente de Servicios del Hogar

> **Proyecto Final - IA: Prompt Engineering para Developers 3.0 (Coderhouse)** > **Autor:** Mateo Bentos

---

## 🌐 Enlace a la Aplicación Desplegada
👉 **[Abrir Servii AI en Streamlit Cloud](https://servii-ai.streamlit.app)** *(Repositorio de GitHub: [https://github.com/Velde01/Proyecto_Final_Servii-AI](https://github.com/Velde01/Proyecto_Final_Servii-AI))*

---

## 📌 Descripción del Proyecto
**Servii AI** es una solución web desarrollada en **Streamlit** e impulsada por los modelos fundacionales de **Google Gemini** para resolver la asimetría de información en el mercado de reparaciones del hogar (sanitaria, electricidad, cerrajería, albañilería, etc.).

A través de técnicas de **System Prompting con Salida Dirigida (Structured Output)**, la aplicación traduce descripciones informales de los usuarios en una **Ficha Técnica Estructurada en formato JSON**, permitiendo presupuestar reparaciones con precisión y evitando visitas técnicas "a ciegas".

---

## 🧪 Ejemplos de Prueba para Testear la App

Podés copiar y pegar cualquiera de estos 3 casos reales en la aplicación para verificar la salida dirigida:

### 🔹 Caso 1: Electricidad (Riesgo / Urgencia Alta)
> *"El calefón eléctrico hace saltar la llave térmica general a los 5 minutos de encenderse y despide un leve olor a plástico caliente."*
* **Resultado esperado:** Categoría: *Electricidad*, Urgencia: *Alta/Crítica*, Profesional: *Electricista*, Materiales: *Resistencia, termostato, multímetro*.

### 🔹 Caso 2: Sanitaria (Urgencia Media)
> *"Tengo una fuga constante de agua debajo de la bacha de la cocina, parece salir de la unión del sifón de PVC."*
* **Resultado esperado:** Categoría: *Sanitaria*, Urgencia: *Media*, Profesional: *Sanitario / Plomero*, Materiales: *Sifón de PVC, teflón, sellador de juntas*.

### 🔹 Caso 3: Cerrajería (Urgencia Alta / Bloqueo)
> *"Se trabó la llave dentro del cerrojo de la puerta principal, giró media vuelta y no sale ni abre."*
* **Resultado esperado:** Categoría: *Cerrajería*, Urgencia: *Alta*, Profesional: *Cerrajero*, Materiales: *Extractor de llaves, cilindro/tambor de repuesto*.

---

## 🧠 Arquitectura del Prompt y Esquema JSON

La aplicación utiliza un prompt estricto con salida forzada en formato JSON válido:

```json
{
  "categoria": "Sanitaria | Electricidad | Cerrajería | Climatización | Albañilería | Pintura | Otro",
  "diagnostico_preliminar": "Explicación técnica de la falla detectada",
  "nivel_urgencia": "Bajo | Medio | Alto | Crítico",
  "profesional_requerido": "Tipo de especialista necesario",
  "materiales_probables": ["material 1", "material 2"],
  "tiempo_estimado_horas": "Rango de tiempo aproximado (ej: 1 a 2 horas)",
  "resumen_para_tecnico": "Resumen técnico formal listo para cotizar"
}