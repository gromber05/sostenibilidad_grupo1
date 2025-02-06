import http.server
import socketserver


PORT = 8000

# Directorio desde el cual se servirán los archivos
DIRECTORIO = r"./"

class Handler(http.server.SimpleHTTPRequestHandler):
    # Cambiar el directorio de trabajo para el servidor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor corriendo en http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
            httpd.server_close()