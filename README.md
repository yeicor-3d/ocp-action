# CadQuery action

This action runs [CadQuery](https://github.com/CadQuery/cadquery) to build your models emulating
the [CQ-editor](https://github.com/CadQuery/CQ-editor).

## Features

- Automatically test your model(s) in your CI/CD pipeline
- Automatically build the latest version of your model(s) for release.
- No boilerplate: use the same code from the [CQ-editor](https://github.com/CadQuery/CQ-editor) and in your CI/CD
  pipeline.
- Build a static website to showcase your latest model(s) automatically.
- Take a screenshot of your model(s) and use it as a preview image.

## Usage

This repository also serves as a demo. A repository that uses this action only needs the python scripts for generating
the models, like the ones in [demos](demos) and the [workflow](.github/workflows/ci.yml).

### Demo: [box.py](demos/box.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/simple_box.png)](https://yeicor.github.io/cadquery-action/)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/simple_box.svg)

### Demo: [cycloidal_gear.py](demos/cycloidal_gear.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/cycloidal_gear.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/cycloidal_gear.gltf)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/cycloidal_gear.svg)

### Demo: [parametric_enclosure.py](demos/parametric_enclosure.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/parametric_enclosure.gltf)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure.svg)