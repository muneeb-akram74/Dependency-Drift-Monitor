import hcl2

def parse_terraform(file_path):
    with open(file_path, 'r') as file:
        return hcl2.load(file)

def get_versions_from_terraform(data):
    versions = {}
    # Iterate over the list of modules
    for module in data.get('module', []):
        # Each module is a dictionary with the module name as the key
        for module_name, module_info in module.items():
            versions[module_name] = {
                'current': module_info.get('version')  # Correctly access the 'version' field
            }
    return versions

