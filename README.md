# Pydra NixUtils package

This repository contains Pydra task interfaces for commonly used *nix tools,
e.g. `tar`, `unzip`, `zip`

Part of this effort is to establish a (mostly) declarative language for describing tasks that
potentially have intricate rules for determining the availability and names from the choice of
inputs.

## Installation
```
pip install /path/to/pydra-nixutils/
```

### Installation for developers
```
pip install -e /path/to/pydra-nixutils/[dev]
```

## Basic Use

To run the `unzip` task

```
from pydra.tasks.nixutils import Unzip

task = Unzip(in_dir='/path/to/zip/file', out_dir='/path/to/extract/output')
result = task()
```

However, utils are typically typically be used as the first step within larger Pydra workflows

```
from pydra import Workflow
from pydra.tasks.nixutils import Unzip

my_workflow = Workflow(name='my_workflow', input_spec=['zip_file'])

my_workflow.add(
    Unzip(name='unzipper', in_dir=my_workflow.lzin.zip_file, out_dir='.'))
my_workflow.add(...)

my_workflow()
```