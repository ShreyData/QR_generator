import sys
import os
# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qr_app.qr_engine import generate_qr_advanced

def test_engine():
    print("Testing Advanced QR Engine...")
    try:
        # Test basic generation
        b64 = generate_qr_advanced("Hello World")
        print(f"Basic generation: Success (Length: {len(b64)})")
        
        # Test customization
        b64_custom = generate_qr_advanced(
            "Custom QR", 
            fill_color="#FF0000", 
            back_color="#FFFF00", 
            module_drawer='circle'
        )
        print(f"Custom generation (red circles on yellow): Success (Length: {len(b64_custom)})")
        
        if b64.startswith("data:image/png;base64,"):
            print("Format validation: PASSED")
        else:
            print("Format validation: FAILED")
            
    except Exception as e:
        print(f"Test FAILED with error: {e}")

if __name__ == "__main__":
    test_engine()
