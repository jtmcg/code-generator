import sys
from src.unittest_solver import UnittestSolver

def main(unittest_path):

    unittestSolver = UnittestSolver(unittest_path, model_name="gpt-4-turbo-preview", temperature=0.5)
    unittestSolver.generate_code()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <unittest_path>")
        sys.exit(1)
    else: 
        main(sys.argv[1])