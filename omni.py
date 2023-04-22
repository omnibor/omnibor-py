import ast
import hashlib
import importlib
import os
import glob
import sys

node_info_set = set()
nodes_unavailable_set = set()

def get_sha1(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


def get_dependencies(module_path):
    if os.path.exists("./__pycache__"):
        pyc_files = glob.glob("." + '/**/*.pyc')
        for f in pyc_files:
            gitoid = "gitoid:blob:sha1:" + get_sha1(f)
            node_info_set.add("node: " + f + " " + gitoid)

    get_sub_dependencies(module_path)
    return node_info_set
        
def get_sub_dependencies(module_path):
    with open(module_path, 'r') as f:
        tree = ast.parse(f.read(), module_path)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for module in node.names:
                # in case something is dynamically loaded
                importlib.invalidate_caches()
                #try block is because the module may not be available
                #like you may need a pip install
                try:
                    imp_name = importlib.import_module(module.name)
                    filename = os.path.basename(imp_name.__file__)
                    hash = get_sha1(imp_name.__file__) 
                    gitoid = "gitoid:blob:sha1:"+hash
                    node_info_set.add("leaf: " + filename + " " + gitoid)
                    # for sub modules
                    if imp_name.__file__.endswith('.py'):
                        return get_dependencies(imp_name.__file__)
                    #else get the hash of the pyd et al file
                except:
                    #Need to handle the case where a module is unavailable
                    nodes_unavailable_set.add(module.name)
                
    return node_info_set

def write_manifest(deps):
    try:
        with open("py_OmniBOR.sha1", "w") as f:
            set_string = '\n'.join(str(element) for element in deps)
            f.write(set_string)
    except:
        print(f"Could not open py_OmniBOR.sh1")

def main():
    # use the 'entry point' to be analyzed
    if len(sys.argv) < 2:
        exit("Enter starting node. Ex: python omni.py entrypoint.py")
    entry_node = sys.argv[1]
    if not  os.path.exists(entry_node):
        exit("File does not exist. Exiting.")
        
    dependencies = get_dependencies(entry_node)
    write_manifest(dependencies)
    #TODO check on stuff below
    if nodes_unavailable_set:
        set_string = '\n'.join(str(element) for element in nodes_unavailable_set)
        print(set_string)

if __name__ == '__main__':
    main()