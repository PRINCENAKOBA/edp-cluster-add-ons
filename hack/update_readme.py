import yaml
from tabulate import tabulate
import os

# Load the main YAML file
with open('./chart/values.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Initialize the list for the table data
table_data = []

# Iterate over the data
for key, value in data.items():
    # Initialize the row data with placeholders
    row = {'Component': key, 'version': 'N/A', 'appVersion': 'N/A', 'createNamespace': value.get('createNamespace', 'N/A'), 'enable': value.get('enable', 'N/A')}

    # Try to open the Chart.yaml file for the component
    try:
        with open(f'./add-ons/{key}/Chart.yaml', 'r') as file:
            chart_data = yaml.safe_load(file)
            row['version'] = chart_data.get('version', 'N/A')
            row['appVersion'] = chart_data.get('appVersion', 'N/A')
    except FileNotFoundError:
        pass

    # Add the row to the table data
    table_data.append(row)

# Generate the markdown table
table = tabulate(table_data, headers='keys', tablefmt='pipe')

# Read the README file
with open('README.md', 'r') as file:
    content = file.read()

# Split the content at the comment
parts = content.split('<!-- AUTOGENERATED CONTENT BELOW -->')

# Replace the second part with the new table
parts[1] = '\n' + table + '\n'

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write('<!-- AUTOGENERATED CONTENT BELOW -->'.join(parts))
