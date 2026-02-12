import os
import sys
from pathlib import Path

# Agregar el directorio de la habilidad al path para importar speak_google
skill_dir = Path(__file__).parent
sys.path.append(str(skill_dir))

try:
    from speak_google import speak
except ImportError:
    print("❌ Error: No se pudo importar speak_google.py")
    sys.exit(1)

def read_text(content):
    """Limpia un poco el markdown y lo lee"""
    # Limpieza básica de markdown para que no lea asteriscos o hashtags
    clean_text = content.replace("#", "").replace("*", "").replace(">", "").strip()
    if clean_text:
        speak(clean_text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if path.exists() and path.is_file():
            with open(path, 'r', encoding='utf-8') as f:
                read_text(f.read())
        else:
            # Si no es archivo, lee el argumento como texto
            read_text(" ".join(sys.argv[1:]))
    else:
        print("Uso: python read_text.py 'texto a leer' o python read_text.py ruta/al/archivo.md")
