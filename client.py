import socket
import click


@click.command()
@click.option("--host", default='127.0.0.1', type=str)
@click.option("--port", default='65432', type=int)
@click.option('--text', prompt='Text to translate to morse', help='The person to greet.', type=str)
def translate(host, port, text):
    """Simple client to connect to the morse server and translate text"""
    click.echo("Sending request to Morse server via socket")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str.encode(text))
        data = s.recv(1024)
    click.echo("Received: {}".format(data.decode('utf-8')))

if __name__ == '__main__':
    translate()