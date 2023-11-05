# OCP action

GitHub Action that builds [OCP](https://github.com/CadQuery/OCP) models ([CadQuery](https://github.com/CadQuery/cadquery)/[Build123d](https://github.com/gumyr/build123d)/...), renders them and sets up a model viewer on Github Pages.

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
the [build artifacts](https://github.com/Yeicor/ocp-action/actions/workflows/ci.yml).

### Demo: [box.py](demos/box.py)

[![Demo](https://yeicor.github.io/ocp-action/models/demos/box/simple_box.png)](https://yeicor.github.io/ocp-action/?model=models/demos/box/simple_box.gltf)

![Demo](https://yeicor.github.io/ocp-action/models/demos/box/simple_box.svg)

### Demo: [cycloidal_gear.py](demos/cycloidal_gear.py)

[![Demo](https://yeicor.github.io/ocp-action/models/demos/cycloidal_gear/cycloidal_gear.png)](https://yeicor.github.io/ocp-action/?model=models/demos/cycloidal_gear/cycloidal_gear.gltf)

![Demo](https://yeicor.github.io/ocp-action/models/demos/cycloidal_gear/cycloidal_gear.svg)

### Demo: [parametric_enclosure.py](demos/parametric_enclosure.py)

[![Demo](https://yeicor.github.io/ocp-action/models/demos/parametric_enclosure/topOfLid.png)](https://yeicor.github.io/ocp-action/?model=models/demos/parametric_enclosure/topOfLid.gltf)

[![Demo](https://yeicor.github.io/ocp-action/models/demos/parametric_enclosure/debug-bottom.png)](https://yeicor.github.io/ocp-action/?model=models/demos/parametric_enclosure/debug-bottom.gltf)

![Demo](https://yeicor.github.io/ocp-action/models/demos/parametric_enclosure/topOfLid.svg)

![Demo](https://yeicor.github.io/ocp-action/models/demos/parametric_enclosure/debug-bottom.svg)

### Demo: [build123d_tea_cup.py](demos/build123d_tea_cup.py)

[![Demo](https://yeicor.github.io/ocp-action/models/demos/build123d_tea_cup/tea_cup.png)](https://yeicor.github.io/ocp-action/?model=models/demos/build123d_tea_cup/tea_cup.gltf)

![Demo](https://yeicor.github.io/ocp-action/models/demos/build123d_tea_cup/tea_cup.svg)