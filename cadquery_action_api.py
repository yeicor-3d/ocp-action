import os
import time
from typing import Union, Dict, Optional

import cadquery as cq

# Retrieve the options
out_dir = os.getenv("CQ_ACTION_OUT_DIR", ".")
def_name = os.getenv("CQ_ACTION_DEF_NAME", "model")
wanted_formats = os.getenv("CQ_ACTION_WANTED_FORMATS", "STL|SVG").split("|")
print(f"cadquery_action_api.py: out_dir={out_dir}, def_name={def_name}, wanted_formats={wanted_formats}")


def show_object(obj: Union[cq.Workplane, cq.Shape], name: Optional[str] = None,
                options: Optional[Dict[str, any]] = None) -> None:
    """Emulates the cq-editor API to build the models instead."""

    name = name or def_name

    # Create the output directory
    os.makedirs(out_dir, exist_ok=True)

    # For each wanted format
    for fmt in wanted_formats:

        # Export the model in the wanted format
        model_name = f"{out_dir}/{name}.{fmt.lower()}"
        print(f"Exporting {model_name}...")

        if fmt == "GLTF":  # Only assemblies support GLTF
            cq.Assembly(obj).save(model_name)
        else:  # Default export
            # noinspection PyTypeChecker
            cq.exporters.export(obj, model_name, fmt)

            # Fix SVG files forcing a white background
            if fmt == "SVG":
                with open(model_name, "r") as f:
                    svg = f.read()
                with open(model_name, "w") as f:
                    f.write(svg.replace(
                        "<g ", '<rect width="99999999%" height="99999999%" fill="white"/><g ', 1))


def show(*args, **kwargs) -> None:
    """Emulates the cq-editor API to build the models instead."""
    # Call the show_object function
    return show_object(*args, **kwargs)


def debug(*args, **kwargs) -> None:
    """Emulates the cq-editor API to build the models instead."""
    # Force the name to be debug-<name>
    if "name" in kwargs:
        kwargs["name"] = "debug-" + kwargs["name"]
    elif len(args) > 1:
        args = list(*args)
        args[1] = "debug-" + args[1]
    else:
        args = list(*args)
        args.append(f"debug-{time.time()}")
    # Call the show_object function
    return show_object(*args, **kwargs)
