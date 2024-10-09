import socket
from urllib.parse import urlparse, parse_qs
from os.path import abspath, dirname
import sys
import csv
import manegDB



SELECT = 0
SET = 1
PRINT = 2

# TODO
def get_resp(q_type, query, db, csv_name):
    if q_type == SELECT:
        return manegDB.get_amount_by_id(db,query)
    elif q_type == SET:

        if check_query(query)==True:
           writing_to_file(csv_name,query)
           return manegDB.upsert_person(db,query)
       
        return check_query(query)
    

    return manegDB.get_amount_by_id(db,query)

def check_query(query):
    try:
        first_name, last_name, phone, id_number, amount ,date = query.split(',')
    except:
        return "Enter data in the correct structure"
    return True
    
import os

def writing_to_file(csv_name, query):
    
    with open(csv_name, "a", encoding='utf-8') as fd:
        fd.write(query + '\n')



def parse_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return parsed_url.path, query_params

def parse_post_body(name, request):
    _, _, body = request.partition("\r\n\r\n")
    idx = body.find(f'name="{name}"')
    if idx < 0:
        return None
    start_idx = idx + len(f'name="{name}"')
    body = body[start_idx:].strip()
    end_idx = body.find("\n")
    return body[:end_idx].strip()

def handle_request(client_socket, csv_file, db):
    # Receive the request
    request = client_socket.recv(2046).decode('utf-8')

    print(request)
    

    request_lines = request.splitlines()
    if request_lines:
        # Extract the HTTP method and url from the request line
        method, url, _ = request_lines[0].split()
        path, params = parse_url(url)
        error = 0

       
        
        # Generate the HTTP response
        # include CRLF (Carriage Return Line Feed) as defined in the HTTP/1.1 specification (RFC 7230)
        if method == 'GET':
            if path == "/":
                dir_path = dirname(abspath(__file__))
                with open(f"{dir_path}/home.html", "r") as f:
                    resp = f.read()
            elif path == "/select":
                query = params.get('select')
                if query is None:
                    error = 1
                else:
                    resp = get_resp(SELECT, query[0], db, csv_file)
            elif path == "/print":
                resp = get_resp(PRINT, "", db, csv_file)
            else:
                error = 1

        elif method == 'POST':
            if path == "/set":
                query = parse_post_body("set", request)
                if query is None:
                    error = 1
                else:
                    resp = get_resp(SET, query, db, csv_file)
            else:
                error = 1
        else:
            error = 2
        
        if not error:
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(resp)}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{resp}"
            )
        elif error == 1:
            response = (
                "HTTP/1.1 404 Page Not Found\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n"
                "\r\n"
                "<html><body><h1>404 Page Not Found</h1></body></html>"
            )
        else:
            response = (
                "HTTP/1.1 405 Method Not Allowed\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n"
                "\r\n"
                "<html><body><h1>405 Method Not Allowed</h1></body></html>"
            )

        # Send the response
        client_socket.sendall(response.encode('utf-8'))
    
    # Close the client connection
    client_socket.close()

def start_server(port=8888):
    if len(sys.argv) < 2:
        print("Error: expected CSV file")
        return
    
    csv_name = sys.argv[1]
    
    with open(csv_name, "r") as fd:
        lines = fd.read().splitlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split(",")
    print(*lines, sep="\n")

    # TODO
    db = manegDB.start()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    
    print(f"Listening on port {port}...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Handle the request
        handle_request(client_socket, csv_name, db)

if __name__ == "__main__":
    
    start_server()