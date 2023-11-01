import argparse
import sys
from datetime import datetime
import configparser
import pytz



def main(nmro, outro_nmro, saida):
    result = nmro * outro_nmro
    fuso_horario = pytz.timezone('America/Sao_Paulo')
    data_formatada= datetime.now(fuso_horario).strftime("%m-%d %H:%M:%S")
    print(f'[{data_formatada}] The result is {result}',file=saida)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', '-c', type=argparse.
                        FileType('r'),
                        help='config file',
                        default='/workspaces/WebScraping/config.ini')
    parser.add_argument('-o', dest='saida', type=argparse.
                        FileType('a'),
                        help='output file',
                        default=sys.stdout)
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Transforming values into integers
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])
    main(args.n1, args.n2, args.saida)
