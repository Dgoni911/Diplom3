import subprocess
import sys

def run_tests():
    cmd = [
        "pytest",
        "tests/",
        "-v",
        "--alluredir=allure-results"
    ]
    
    result = subprocess.run(cmd)
    return result.returncode

if __name__ == "__main__":
    return_code = run_tests()
    sys.exit(return_code)