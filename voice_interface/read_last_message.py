import os
import sys

# Import speak function
try:
    from speak_google import speak
except ImportError:
    print("❌ Error: speak_google.py not found.")
    sys.exit(1)

# Path to last message file
LAST_MESSAGE_FILE = os.path.join(os.path.dirname(__file__), "last_agent_message.txt")

def read_last_message():
    """
    Reads the last message sent by the agent and speaks it aloud.
    """
    if not os.path.exists(LAST_MESSAGE_FILE):
        speak("No hay mensajes previos guardados.")
        return
    
    try:
        with open(LAST_MESSAGE_FILE, 'r', encoding='utf-8') as f:
            last_msg = f.read().strip()
        
        if last_msg:
            print(f"🗣️ Leyendo último mensaje:\n{last_msg}\n")
            speak(last_msg)
        else:
            speak("El último mensaje está vacío.")
    
    except Exception as e:
        print(f"❌ Error leyendo mensaje: {e}")
        speak("Hubo un error al leer el último mensaje.")

if __name__ == "__main__":
    read_last_message()
