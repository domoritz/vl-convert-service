from http.server import BaseHTTPRequestHandler
from urllib import parse
import vl_convert as vlc

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        query_params = dict(parse.parse_qsl(parse.urlsplit(s).query))

        # Extract query params
        vl_spec = query_params.get("vl_spec")
        vl_version = query_params.get("vl_version", None)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        vg_spec = vlc.vegalite_to_vega(vl_spec, vl_version=vl_version)
        self.wfile.write(vg_spec.encode())
        return