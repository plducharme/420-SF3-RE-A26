import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:

    serveur.bind(("10.18.4.142", 8888))
    serveur.listen()

    conn, adresse = serveur.accept()
    print(f"connexion reçu de {adresse}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Reçu: {data}")


