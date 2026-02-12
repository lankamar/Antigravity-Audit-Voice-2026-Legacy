import json
import os
from pathlib import Path

state_file = Path(r"C:\Users\Teresa\.gemini\antigravity\skills\skills\notebooklm\data\browser_state\state.json")
auth_dir = Path(r"C:\Users\Teresa\.notebooklm-mcp")
auth_file = auth_dir / "auth.json"

if state_file.exists():
    with open(state_file, 'r') as f:
        state = json.load(f)
    
    cookies = state.get("cookies", [])
    
    auth_dir.mkdir(parents=True, exist_ok=True)
    with open(auth_file, 'w') as f:
        json.dump(cookies, f, indent=2)
    
    print(f"Migradas {len(cookies)} cookies a {auth_file}")
else:
    print("No se encontró el archivo de estado original.")
