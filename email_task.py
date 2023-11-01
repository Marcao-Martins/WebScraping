import argparse
import configparser
import smtplib
from email.message import EmailMessage
import logging

# Configuração do logging para escrever em um arquivo
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%D %H:%M:%S')

def main(to_email, server, port, from_email, password):
    try:
        print(f'With love, from {from_email} to {to_email}')

        subject = 'With Love from ME to YOU'
        text = '''teste'''
        msg = EmailMessage()
        msg.set_content(text)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        server = smtplib.SMTP_SSL(server, port)
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        logging.error('Failed to send email: %s', e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='destination email')
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'), help='config file', default=None)
    args = parser.parse_args()
    if not args.config:
        print('Error, a config file is required')
        parser.print_help()
        exit(1)
    config = configparser.ConfigParser()
    config.read_file(args.config)
    main(args.email, server=config['DEFAULT']['server'], port=config['DEFAULT']['port'], from_email=config['DEFAULT']['email'], password=config['DEFAULT']['password'])

