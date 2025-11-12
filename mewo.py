import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    parser.add_argument('-n', default= 1, type=int, help='Name to greet')
    args = parser.parse_args()
    for i in range(args.n):
        print("Hello, World!")
if __name__ == "__main__":
    main()
