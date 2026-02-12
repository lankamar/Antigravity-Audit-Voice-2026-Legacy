import os
import sys
from pathlib import Path
from gtts import gTTS

# Directorio de la habilidad de voz
VOICE_DIR = Path(r"C:\Users\Teresa\.gemini\antigravity\skills\voice_interface").resolve()
BUFFER_FILE = VOICE_DIR / "last_agent_message.txt"
AUDIO_FILE = VOICE_DIR / "last_message.mp3"

def save_message(text):
    """Guarda el texto y genera el audio MP3"""
    try:
        if not VOICE_DIR.exists():
            VOICE_DIR.mkdir(parents=True, exist_ok=True)
            
        # Guardar Texto
        with open(BUFFER_FILE, 'w', encoding='utf-8') as f:
            f.write(text)
            
        print(f"📄 Texto guardado en: {BUFFER_FILE}")
            
        # Generar Audio
        print(f"🎙️ Generando audio MP3...")
        tts = gTTS(text=text, lang='es')
        tts.save(str(AUDIO_FILE))
        print(f"✅ Audio generado en: {AUDIO_FILE}")
        
        return True
    except Exception as e:
        print(f"❌ Error guardando mensaje/audio: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        save_message(message)
    else:
        print("Uso: python save_message.py 'texto'")
