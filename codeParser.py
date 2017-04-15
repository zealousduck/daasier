
import json
import ast
import urllib.request

def getFuncDefJSON(node):
    ins = [f[1] for a in ast.iter_child_nodes(node.args) for f in ast.iter_fields(a) if f[0] == 'arg']

    return {
        "name":node.name,
        "docString":ast.get_docstring(node),
        "input":ins,
    }

def getClassDefJSON(node):
    funcs = [getFuncDefJSON(n) for n in node.body if isinstance(n, ast.FunctionDef)]
    return {
        "class": {
            "name":node.name,
            "docString":ast.get_docstring(node),
            "funcs":funcs
            }
    }

def getModuleFuncJSON(nodeList):
    funcs = [getFuncDefJSON(n) for n in nodeList]
    return {
        "module": {
            "funcs":funcs
            }
    }

def code_to_json(url):
    code = urllib.request.urlopen(url).read().decode('utf-8')
    prog = ast.parse(code)

    class_def = [node for node in ast.iter_child_nodes(prog) if isinstance(node, ast.ClassDef)]
    classJSON = [getClassDefJSON(cl) for cl in class_def]

    module_func = [node for node in ast.iter_child_nodes(prog) if isinstance(node, ast.FunctionDef)]
    moduleJSON = getModuleFuncJSON(module_func)

    codeJSON = {
        "file":url,
        "classes":classJSON,
        "moduleFuncs":moduleJSON,
        }

    return json.JSONEncoder().encode(codeJSON)

if __name__ == "__main__":
    parsed = code_to_json('https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/python/framework/device.py')
    print(parsed)
