import streamlit as st
import google.generativeai as genai
import os

# Configuración de la página
st.set_page_config(
    page_title="EmploBot - Asistente de Empleabilidad",
    page_icon="💼",
    layout="centered"
)

# Prompt del sistema
PROMPT_SISTEMA = """Eres "EmploBot", un consultor especializado en empleabilidad y desarrollo profesional. 
Tu función es ayudar a las personas a mejorar sus oportunidades laborales.

Objetivo:
- Preparar a los usuarios para entrevistas de trabajo
- Evaluar y mejorar sus competencias profesionales
- Orientar en su búsqueda laboral

Instrucciones:
- Responde siempre en español
- Sé profesional pero cercano y amigable
- Da consejos prácticos, específicos y accionables
- Haz preguntas de seguimiento para entender mejor al usuario
- Adapta tus respuestas al perfil y experiencia del usuario
- Usa ejemplos concretos cuando sea posible

Restricciones:
- NO des consejos legales, médicos o de salud mental
- NO hagas promesas de empleo o resultados garantizados
- Si no sabes algo, admítelo honestamente"""

# Configurar Gemini API
def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)
    if not api_key:
        st.error("⚠️ No se encontró la API Key de Gemini. Por favor, configúrala en los secrets de Streamlit.")
        st.stop()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=PROMPT_SISTEMA
    )

# Inicializar sesión
def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat" not in st.session_state:
        model = configure_gemini()
        st.session_state.chat = model.start_chat(history=[])

# Mostrar mensaje de chat
def display_message(role, content):
    with st.chat_message(role):
        st.markdown(content)

# Barra lateral
def sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/briefcase.png", width=80)
        st.title("EmploBot")
        st.caption("Asistente de Empleabilidad")
        st.divider()
        st.markdown("""
        **Áreas de ayuda:**
        - 🎯 Preparación para entrevistas
        - 📊 Revisión de competencias
        - 🔍 Orientación laboral
        """)
        st.divider()
        if st.button("🗑️ Limpiar conversación"):
            st.session_state.messages = []
            model = configure_gemini()
            st.session_state.chat = model.start_chat(history=[])
            st.rerun()
        st.divider()
        st.caption("Desarrollado con Python + Gemini API + Streamlit")

# Mensaje de bienvenida
def welcome_message():
    if not st.session_state.messages:
        welcome = """¡Hola! Soy **EmploBot**, tu consultor de empleabilidad. 👋

Estoy aquí para ayudarte con:

- **Preparación para entrevistas** - Practica preguntas y recibe retroalimentación
- **Revisión de competencias** - Evalúa tus habilidades y áreas de mejora
- **Orientación laboral** - Consejos para tu búsqueda de empleo

¿En qué puedo ayudarte hoy?"""
        display_message("assistant", welcome)

# App principal
def main():
    st.title("💼 EmploBot - Chatbot de Empleabilidad")
    st.caption("Tu asistente personal para prepación laboral y desarrollo profesional")
    
    sidebar()
    init_session()
    welcome_message()
    
    # Mostrar historial de mensajes
    for message in st.session_state.messages:
        display_message(message["role"], message["content"])
    
    # Input del usuario
    if prompt := st.chat_input("Escribe tu mensaje aquí..."):
        # Mostrar y guardar mensaje del usuario
        display_message("user", prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Generar respuesta
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    response = st.session_state.chat.send_message(prompt)
                    answer = response.text
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    error_msg = "Lo siento, hubo un error al procesar tu mensaje. Por favor, intenta de nuevo."
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

if __name__ == "__main__":
    main()
