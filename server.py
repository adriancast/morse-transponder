#!/usr/bin/env python3
import socket
import click

from transponder.client import MorseTransponder

@click.command()
@click.option("--host", default='127.0.0.1', type=str)
@click.option("--port", default='65432', type=int)
def serve(host, port):
    print('Waiting socket connections at host {}:{}'.format(host, port))
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    transponder = MorseTransponder()
                    morse_text = transponder.translate_to_morse_and_play_audio(text=data.decode('utf-8'))
                    print('Sending text "{}" translated to "{}" to address {}'.format(data.decode('utf-8'), morse_text, addr))

                    conn.sendall(str.encode(morse_text))

if __name__ == '__main__':
    serve()