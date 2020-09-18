![alt text](https://img.shields.io/github/license/hagaika/Configs-dev)
![alt version-badge](https://img.shields.io/badge/dynamic/yaml?color=blue&label=version&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fhagaika%2FConfigs-dev%2Fmaster%2Fpackage.yaml&logo=appveyor)
[![Build Status](https://www.travis-ci.org/hagaika/Configs-dev.svg?branch=master)](https://www.travis-ci.org/hagaika/Configs-dev)
![alt open-issues-badge](https://img.shields.io/github/issues-raw/hagaika/Configs-dev)
[![Documentation Status](https://readthedocs.org/projects/configs-dev/badge/?version=latest)](https://configs-dev.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/hagaika/Configs-dev/shield.svg)](https://pyup.io/repos/github/hagaika/Configs-dev/)
[![Python 3](https://pyup.io/repos/github/hagaika/Configs-dev/python-3-shield.svg)](https://pyup.io/repos/github/hagaika/Configs-dev/)




# Configs-dev
This project is all about configuration setup!

**Configs-dev** is a fast and easy to use configuration management library for python.
It offers an abstraction for your application configuration, with an efficient and clean implementation.

## Features and benefits
Using **Configs-dev** would allow you to manage all configurations in your application with ease and without the need to make any DB queries.

_**<ins>Features:</ins>**_
1. Define configuration hierarchy either from a YAML file or code
2. Safely adding conflict-free new configurations
3. Safely editing both configuration and hierarchies
4. Fetching configurations and default values with ease

## Documentation
Click view the [**full documentation**](https://configs-dev.readthedocs.io/en/latest/)

## Quick Start
To begin using **Config-dev** you would need to define an hierarchy for your configurations.

An hierarchy defines the structure of your configurations and what are the default values.
_It may be seen as your business logic structure._

For example sake I have a network of pizza places on different areas.

ADD EXAMPLE HERE

### Setting my configuration file
`layers.yaml:`

    app: pizzaplace             # name of the app
    layers:                     # app layers set-up 
      - name: area              # name of first layer
        children:               # childs of first layer
          - name: branch        # name of second layer
            children:           
              - name: pizza     # name of third layer
              - name: oven      # name of another third layer

In this example we have a top layer of area, which define there are several areas.
Second layer is branch, that implicitly tells **Configs-dev** that areas contain several branches, and if a 
configuration was not found for a specific branch it will ask the area for that configuration.
Each branch has pizza configuration and oven configurations that would act the same and it can go on and on.
No limits on the complexity of your application configuration.

In general each layer have:
* Unique name - _**Must**_
* Child layers - _Optional_

## Package maintainers
This package is delivered with :heart: and maintained by AppCard inc.

The use of is according to the LICENSE

