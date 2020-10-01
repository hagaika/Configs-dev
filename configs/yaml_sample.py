"""
This is a sample script for using 'strictyaml' package
Maybe use deepdiff for changes check

TODO:
    1. Create a class for functionality API
    2. Create an Exceptions for errors
    3. Make tests
"""

from strictyaml import Map, Any, Str, Seq, Optional, load
from strictyaml.exceptions import YAMLValidationError
from anytree import Node, RenderTree, AnyNode
from anytree.importer import DictImporter
from collections.abc import Sequence
from os import path


class BadYAMLError(AssertionError):
    # TODO: add informative error cause
    pass


class Structure:
    __scheme = Map({
        'app': Str(),
        'layers': Seq(
            Map({
                'name': Str(),
                Optional('children'): Seq(Any())
            })
        )
    })

    def __init__(self):
        self.__file = None
        self.__global_layer = None

    @property
    def layers(self):
        return self.__global_layer

    def structure_from_file(self, absolute_file_path: str):
        self.__file_exist(absolute_file_path)
        try:
            with open(absolute_file_path, 'r') as file:
                raw_yaml = file.read()
            output_yaml = load(raw_yaml, self.__scheme)
            self.__validate_layer_children(output_yaml.data['layers'], [])
        except YAMLValidationError as ye:
            # TODO log error, handle more error types
            raise BadYAMLError
        except AssertionError as ae:
            raise BadYAMLError

        global_dict = dict()
        global_dict['name'] = 'global'
        global_dict['children'] = output_yaml.data['layers']

        self.__file = absolute_file_path
        self.__global_layer = DictImporter().import_(global_dict)

        return self

    def show_structure(self) -> str:
        if self.__global_layer:
            return str(RenderTree(self.__global_layer))
        return 'Structure yet to be defined.'

    @classmethod
    def __file_exist(cls, file_path: str):
        if not isinstance(file_path, str) or not file_path.endswith(('.yml', '.yaml')):
            # TODO: add exception reason
            raise BadYAMLError()
        if not path.isfile(file_path):
            raise BadYAMLError()

    @classmethod
    def __validate_layer_children(cls, chunk, name_memo):
        for layer in chunk:
            assert 'name' in layer
            assert isinstance(layer['name'], str)
            assert layer['name'] not in name_memo
            name_memo.append(layer['name'])

            def _seq_but_not_str(obj):
                return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))

            if 'children' in layer:
                assert _seq_but_not_str(layer['children'])
                cls.__validate_layer_children(layer['children'], name_memo)

    def flatten_layers(self) -> list:
        """
        method to flatten the structure as if searched with BFS

        :return: list of flatten nodes by layers
        """
        if self.layers:
            from anytree import LevelOrderIter
            return [node for node in LevelOrderIter(self.layers)]
        raise Exception('No structure defined')
