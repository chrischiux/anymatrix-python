# cli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Your module description')
    parser.add_argument('--option', type=str, help='An example option')
    args = parser.parse_args()
    
    # Your code here
    print(f'Option value: {args.option}')

if __name__ == '__main__':
    main()