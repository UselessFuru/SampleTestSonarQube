import os
import subprocess

# Hardcoded credentials (Security Hotspot)
DB_PASSWORD = "supersecret123"

def read_file(path):
    # Bug: no validation, possible path traversal
    with open(path, "r") as f:
        return f.read()

def run_command(cmd):
    # Security Hotspot: dangerous use of shell=True
    return subprocess.Popen(cmd, shell=True)

def calculate_discount(price, percent):
    # Bug: percent can be >100 or negative
    return price - (price * percent / 100)

def unused_function(a, b):
    # Code smell: unused function
    return a + b

def main():
    filename = input("Enter filename: ")
    print(read_file(filename))  # Potential vulnerability

    cmd = input("Enter command: ")
    run_command(cmd)  # Security issue

    # Duplicate logic (Sonar will detect)
    total = calculate_discount(100, 10)
    print("Total:", total)

    total2 = calculate_discount(200, 10)
    print("Total2:", total2)

if __name__ == "__main__":
    main()