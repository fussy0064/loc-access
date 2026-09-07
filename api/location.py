from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        data = json.loads(body)

        lat = data.get("lat")
        lon = data.get("lon")
        accuracy = data.get("accuracy")

        result = {
            "status": "ok",
            "lat": lat,
            "lon": lon,
            "accuracy": accuracy,
            "message": f"Location received: {lat}, {lon} (accuracy {accuracy}m)"
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())
