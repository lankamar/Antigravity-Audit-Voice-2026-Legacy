import sys
import os
from gtts import gTTS
import pygame
import time

# Force UTF-8 stdout for Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def speak(text, lang='es'):
    """
    Generates and plays audio from text using Google TTS and pygame.
    """
    print(f"🗣️  Generando audio: '{text}'")
    
    try:
        # Generate audio using Google's native TTS
        tts = gTTS(text=text, lang=lang)
        temp_file = os.path.join(os.path.dirname(__file__), "temp_voice.mp3")
        tts.save(temp_file)
        
        # Initialize mixer
        pygame.mixer.init()
        time.sleep(0.2)  # Pequeña espera para Windows
        pygame.mixer.music.load(temp_file)
        
        print("▶️  Reproduciendo...")
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        pygame.mixer.quit()
        
        # Cleanup
        try:
            os.remove(temp_file)
        except Exception:
            pass 
            
    except Exception as e:
        print(f"❌ Error en interfaz de voz: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_to_speak = " ".join(sys.argv[1:])
        speak(text_to_speak)
    else:
        print("Usage: python speak_google.py 'Texto para hablar'")
