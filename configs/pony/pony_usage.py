import sys

from pony.orm import db_session

from configs.pony.pony_config import Layer, Configuration, Agent, AgentConfiguration, OrmError, \
    TransactionIntegrityError
from configs.pony import db
from pony import orm
from configs.yaml_sample import Structure


def insert_layer(layer_name: str, parent_layer: str = None):
    try:
        with db_session:
            Layer(name=layer_name, parent_layer=parent_layer)

    except TransactionIntegrityError as e:
        print("IntegrityError: UNIQUE constraint failed: Layer.name", file=sys.stderr)
    except OrmError as e:
        print(e, file=sys.stderr)
        return False

    return True


def insert_structure(structure: Structure):
    # do something if structure is empty
    # To be exported to different function
    flatten_layers = structure.flatten_layers()
    layers = []

    for structure_layer in flatten_layers:
        db_layer = Layer(name=structure_layer.name, parent_layer=structure_layer.parent)
        layers.append(db_layer)








def start_db_session(url: str = ':memory:'):
    kwargs = None
    # TODO parse the url to proper connection (postgres, mysql, etc...)
    kwargs = {
        'provider': 'sqlite',
        'filename': ':memory:'
    }
    db.bind(**kwargs)


start_db_session()
db.generate_mapping(create_tables=True)

insert_layer('name')
insert_layer('name')
