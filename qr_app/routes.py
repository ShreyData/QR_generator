from flask import Blueprint, render_template, request, jsonify
from qr_app.qr_engine import generate_qr_advanced

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint for Render."""
    return jsonify({"status": "healthy"}), 200

@routes.route("/api/generate", methods=["POST"])
def api_generate():
    """
    API endpoint to generate an advanced QR code.
    Expects JSON payload with:
    - qr_data (required)
    - fill_color (optional, default: black)
    - back_color (optional, default: white)
    - shape (optional: square, circle, rounded, gapped. default: square)
    - logo (optional, base64 string)
    """
    try:
        data = request.json
        if not data or 'qr_data' not in data:
            return jsonify({"error": "Missing 'qr_data' in request body"}), 400
        
        qr_text = data.get('qr_data')
        fill_color = data.get('fill_color', 'black')
        back_color = data.get('back_color', 'white')
        shape = data.get('shape', 'square')
        logo = data.get('logo') # Base64
        
        qr_image_base64 = generate_qr_advanced(
            data=qr_text,
            fill_color=fill_color,
            back_color=back_color,
            module_drawer=shape,
            logo_base64=logo
        )
        
        return jsonify({
            "success": True,
            "image": qr_image_base64
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@routes.route("/generate", methods=["POST"])
def generate():
    # Deprecated traditional form route, forwarding to advanced engine for compatibility
    data = request.form.get("qr_data")
    filename = "legacy_not_supported.png" # We are moving away from local files
    # For now, let's just render the result with a base64 string if possible, 
    # but the goal is the decoupled frontend.
    qr_image_base64 = generate_qr_advanced(data)
    return render_template("result.html", qr_base64=qr_image_base64)
