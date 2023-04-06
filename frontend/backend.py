import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

backend_dir = os.path.join(current_dir, '..', 'backend')

sys.path.append(backend_dir)

from db import *

sys.path.append(current_dir)

print(models.Appointment)