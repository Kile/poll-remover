import os
import importlib.util

# Define a list to store all the Cog objects
all_cogs = []

# Get the current directory of this __init__.py file
current_dir = os.path.dirname(__file__)

# Loop through all files in the directory
for file_name in os.listdir(current_dir):
    # Check if the file is a Python file and not __init__.py itself
    if file_name.endswith('.py') and not file_name.startswith('__init__.'):
        # Construct the full path to the Python file
        file_path = os.path.join(current_dir, file_name)
        
        # Load the module using importlib
        spec = importlib.util.spec_from_file_location(file_name[:-3], file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if the module has a variable named "Cog"
        if hasattr(module, 'Cog'):
            # Add the Cog object to the list
            all_cogs.append(module.Cog)