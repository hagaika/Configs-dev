"""
This is a sample script for using 'strictyaml' package
Maybe use deepdiff for changes check
"""

# Reading the whole yaml file and getting it as a long string
with open('../layers.yaml', 'r') as f:
    yaml_snippet = f.read()

# importing stringyaml necessary stuff
from strictyaml import Map, Any, Str, Seq, Optional, load

scheme = Map({
    'layers': Seq(
        Map({
            'name': Str(),
            Optional('children'): Seq(Any())
        })
    )
})

output_yaml = load(yaml_snippet, scheme)
print(output_yaml.as_yaml())
print('-' * 10 + ' ' * 3 + 'ORIGINAL' + ' ' * 3 + '-' * 10)
print(yaml_snippet)

# using anytree
from anytree import Node, RenderTree
from anytree.importer import DictImporter
from pprint import pprint

data_yaml = output_yaml.data['layers']


def validate_layer_children(chunk, name_memo):
    for layer in chunk:
        assert 'name' in layer
        assert isinstance(layer['name'], str)
        assert layer['name'] not in name_memo
        name_memo.append(layer['name'])

        from collections.abc import Sequence

        def _seq_but_not_str(obj):
            return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))

        if 'children' in layer:
            assert _seq_but_not_str(layer['children'])
            validate_layer_children(layer['children'], name_memo)


validate_layer_children(data_yaml, [])

pprint(data_yaml)
global_dict = dict()
global_dict['name'] = 'global'
global_dict['children'] = output_yaml.data['layers']
pprint('-' * 10 + 'Global Print')
pprint(global_dict)


class MyNode(Node):
    separator = u' \u27f6 '


root2 = DictImporter().import_(global_dict)
print(RenderTree(root2))
