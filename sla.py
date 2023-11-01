import argparse
def main(number,str):
    print( str * number)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-wtp', type=str, help='What to print',default="ucuc")
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-U',action='store_true',default=False, dest='maiusculo',help='Deixa grande')
    args = parser.parse_args()
    if args.maiusculo:
        args.wtp = args.wtp.upper()
    main(args.number,args.wtp)
