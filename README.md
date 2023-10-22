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

This repository also serves as a demo.

The only requirements are a python script to build the model and a [workflow](.github/workflows/ci.yml) to run the
action.

You can use links similar to the following sections to embed your model in your README.md and point to the interactive
model viewer. The latest models can be downloaded from
the [build artifacts](https://github.com/yeicor/cadquery-action/actions).

### Demo: [box.py](demos/box.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/box/simple_box.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/box/simple_box.gltf)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/box/simple_box.svg)

### Demo: [cycloidal_gear.py](demos/cycloidal_gear.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/cycloidal_gear/cycloidal_gear.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/cycloidal_gear/cycloidal_gear.gltf)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/cycloidal_gear/cycloidal_gear.svg)

### Demo: [parametric_enclosure.py](demos/parametric_enclosure.py)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure/topOfLid.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/parametric_enclosure/topOfLid.gltf)

[![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure/debug-bottom.png)](https://yeicor.github.io/cadquery-action/?model=models/demos/parametric_enclosure/debug-bottom.gltf)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure/topOfLid.svg)

![Demo](https://yeicor.github.io/cadquery-action/models/demos/parametric_enclosure/debug-bottom.svg)