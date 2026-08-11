"""Mock server que imita a API da Apify para validar o ApifyLeadSource real.

Imita:
  POST /v2/acts/{actor}/runs?token=KEY   -> retorna run com defaultDatasetId
  GET  /v2/datasets/{id}/items?token=KEY -> retorna itens no formato do
       google-maps-scraper (title, categoryName, phoneNumbers, placeId)

Uso: python mock_apify.py  (escuta :9100). Aponte APIFY_BASE para ele.
"""
import json
import http.server
import socketserver

PORT = 9100
DATASET = [
    {"title": "Mercado Bom Preço", "categoryName": "Mercado",
     "phoneNumbers": ["+555132165498"], "placeId": "m1"},
    {"title": "Auto Peças Rápidas", "categoryName": "Auto Peças",
     "phoneNumbers": ["+555198732145"], "placeId": "a1"},
]


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if "/acts/" in self.path and "/runs" in self.path:
            self._send(201, {"data": {"id": "run_1", "defaultDatasetId": "ds_1"}})
        else:
            self._send(404, {})

    def do_GET(self):
        if "/datasets/" in self.path and "/items" in self.path:
            self._send(200, DATASET)
        else:
            self._send(404, {})


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", PORT), H) as srv:
        print(f"mock apify em :{PORT}")
        srv.serve_forever()
