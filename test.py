

print("Hello")

try:
    import numpy
    print("The venv is working!")
except ImportError:
    print("Failure")