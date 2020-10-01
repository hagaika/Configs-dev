from datetime import datetime

from pony.orm import *
from configs.pony import db, debug_on

set_sql_debug(debug_on)


class Layer(db.Entity):
    name = PrimaryKey(str)
    child_layer = Set('Layer', reverse='parent_layer')
    parent_layer = Optional('Layer', reverse='child_layer')

    configurations = Set('Configuration')
    agents = Set('Agent')


class Configuration(db.Entity):
    name = PrimaryKey(str)
    min_layer = Required(Layer)
    type = Required(int)  # should be some enum
    allowed_values = Required(str)
    description = Optional(str, default='No description :(')
    created_at = Optional(datetime, default=datetime.now())  # maybe change to timezoned
    default_value = Required(str)

    agents_configurations = Set('AgentConfiguration')


class Agent(db.Entity):
    name = PrimaryKey(str)
    layer = Required(Layer)
    child_agent = Set('Agent', reverse='parent_agent')
    parent_agent = Optional('Agent', reverse='child_agent')

    agents_configurations = Set('AgentConfiguration')


class AgentConfiguration(db.Entity):
    configuration_name = Required(Configuration)
    agent_name = Required(Agent)
    PrimaryKey(configuration_name, agent_name)

    value = Required(str)
    created_at = Optional(datetime, default=datetime.now())


# db.bind(provider='sqlite', filename=':memory:')
# db.generate_mapping(create_tables=True)
