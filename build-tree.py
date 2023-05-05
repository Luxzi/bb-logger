import os, argparse

parser = argparse.ArgumentParser(prog='build-tree', description='Custom script for building nested rust crates', epilog='No you will not get support for this.')
parser.add_argument('-R', '--release', action='store_true', help='Compile as release')
parser.add_argument('-D', '--dev', action='store_true', help='Compile as dev')
args = parser.parse_args()

release = args.release
dev = args.dev

if release and dev == False:
    os.system("cargo build")
    os.chdir("bb_logger_examples")
    os.system("cargo build")
elif release == True:
    os.system("cargo build --release")
    os.chdir("bb_logger_examples")
    os.system("cargo build --release")
else:
    os.system("cargo build")
    os.chdir("bb_logger_examples")
    os.system("cargo build")

