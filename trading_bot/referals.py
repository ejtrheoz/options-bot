import json

def load_refs():
    with open('refs.json', 'r') as f:
        loaded_refs = json.load(f)
        return loaded_refs

def write_refs(refs):
    with open('refs.json', 'w') as f:
        json.dump(refs, f)



refs = load_refs()

