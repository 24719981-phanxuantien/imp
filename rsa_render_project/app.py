import os
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/process")
def process():
    data = request.get_json(silent=True) or {}
    operation = data.get("operation", "")
    content = data.get("content", "")
    key = data.get("key", "")

    if operation not in ("encrypt", "decrypt"):
        return jsonify(error="Vui lòng chọn mã hóa hoặc giải mã."), 400
    if not isinstance(content, str) or not content.strip():
        return jsonify(error="Vui lòng nhập nội dung cần xử lý."), 400
    if not isinstance(key, str) or not key.strip():
        return jsonify(error="Vui lòng nhập khóa RSA."), 400

    executable = os.path.join(os.path.dirname(__file__), "rsa")
    if not os.path.isfile(executable):
        return jsonify(error="Chương trình C chưa được biên dịch. Hãy kiểm tra Build Command trên Render."), 500

    try:
        result = subprocess.run(
            [executable, operation, content, key],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False
        )
        if result.returncode != 0:
            return jsonify(error=result.stderr.strip() or "Không thể xử lý dữ liệu."), 400
        return jsonify(result=result.stdout.rstrip("\n"))
    except subprocess.TimeoutExpired:
        return jsonify(error="Yêu cầu xử lý quá thời gian cho phép."), 408
    except Exception:
        app.logger.exception("RSA processing failed")
        return jsonify(error="Có lỗi xảy ra khi xử lý."), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
