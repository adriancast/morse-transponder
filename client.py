import socket
import click
from transponder.utils import translate_to_alphabet


@click.command()
@click.option("--host", default='127.0.0.1', type=str)
@click.option("--port", default='65432', type=int)
@click.option('--text', prompt='Text to translate to morse', help='The text will be send to the morse server and get translated', type=str)
def translate(host, port, text):
    """Simple client to connect to the morse server and translate text"""
    print("Sending request to Morse server via socket")
    print('Requesting text "{}" to morse transponder server'.format(text))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str.encode(text))
        data = s.recv(1024).decode('utf-8')
        print("Received: {}".format(data))
        print('Translated morse message: "{}"'.format(translate_to_alphabet(data)))

if __name__ == '__main__':
    translate()