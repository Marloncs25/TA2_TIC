# EmploBot - Chatbot de Empleabilidad

Asistente virtual especializado en ayudar a profesionales a mejorar sus oportunidades laborales.

## Funcionalidades

- **Preparación para entrevistas**: Practica preguntas técnicas y recibe retroalimentación
- **Revisión de competencias**: Evalúa tus habilidades y áreas de mejora
- **Orientación laboral**: Consejos para tu búsqueda de empleo

## Tecnologías

- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para crear la interfaz web
- **Google Gemini API**: Inteligencia artificial para generación de respuestas

## Estructura del Proyecto

```
TA2_TIC/
├── app.py                  # Archivo principal del chatbot
├── requirements.txt        # Dependencias Python
├── .streamlit/
│   └── config.toml         # Configuración de Streamlit
└── docs/
    ├── prompt_inicial.md   # Prompt con rol y restricciones
    ├── prueba_1.md         # Test: Preparación entrevista
    ├── prueba_2.md         # Test: Revisión competencias
    ├── prueba_3.md         # Test: Orientación laboral
    └── mejoras.md          # Documento de mejoras
```

## Instalación Local

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar API key de Gemini como variable de entorno
4. Ejecutar:
   ```bash
   streamlit run app.py
   ```

## Despliegue en Streamlit Cloud

1. Subir código a GitHub
2. Conectar con Streamlit Cloud
3. Configurar API key en Secrets
4. Obtener enlace público

## Documentación

Ver carpeta `docs/` para:
- Prompt inicial del chatbot
- Pruebas realizadas
- Problemas y mejoras aplicadas
