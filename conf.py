import os
import json

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')) as handle:
        config = json.load(handle)
except IOError:
    config = {
        'project_name': 'project',
        'secret_key': 'your-secret-key'
    }
