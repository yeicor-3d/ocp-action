import os
import time
from typing import Union, Dict, Optional

import cadquery as cq
from OCP.TopoDS import TopoDS_Shape

# Retrieve the options
out_dir = os.getenv("OCP_ACTION_OUT_DIR", ".")
def_name = os.getenv("OCP_ACTION_DEF_NAME", "model")
wanted_formats = os.getenv(
    "OCP_ACTION_WANTED_FORMATS", "STL|GLTF|SVG").split("|")
tolerance = float(os.getenv("OCP_ACTION_TOLERANCE", "0.1"))
angular_tolerance = float(os.getenv("OCP_ACTION_ANGULAR_TOLERANCE", "0.1"))


class WrappedShape:
    """It is common (cadquery, build123d) to wrap the OCP shapes in a class to add some metadata."""
    wrapped: TopoDS_Shape


class WrappedPartShape:
    """It is common (build123d) to wrap the OCP shapes in a class to add some metadata."""
    part: WrappedShape


def show_object(obj: Union[TopoDS_Shape, WrappedShape, WrappedPartShape, cq.Workplane], name: Optional[str] = None,
                options: Optional[Dict[str, any]] = None) -> None:
    """Emulates the cq-editor API to build the models instead."""

    # Convert any OCP-like object to a cadquery object
    if hasattr(obj, "part"):  # build123d
        obj = obj.part
    if hasattr(obj, "wrapped"):  # cadquery / build123d
        obj = obj.wrapped
    if isinstance(obj, TopoDS_Shape):
        obj = cq.Shape(obj)

    name = name or def_name

    # Create the output directory
    os.makedirs(out_dir, exist_ok=True)

    # Convert Z-up to Y-up (more common?)
    # obj = obj.rotateAboutCenter((1, 0, 0), -90)

    # For each wanted format
    for fmt in wanted_formats:

        # Export the model in the wanted format
        model_path = f"{out_dir}/{name}.{fmt.lower()}"
        # Avoid collisions
        for i in range(1, 1000):
            if not os.path.exists(model_path):
                break
            model_path = f"{out_dir}/{name}-{i}.{fmt.lower()}"
        print(f"Exporting {model_path}...")
        if os.path.exists(model_path):
            print(f"WARNING: {model_path} already exists, overwriting it...")

        if fmt == "GLTF":  # Only assemblies support GLTF
            # Add color if specified
            color = None
            if "color" in (options or {}):
                color = cq.Color(
                    *options["color"], a=options["alpha"] if "alpha" in options else 1)

            # Create a fake assembly just to export it as gltf
            try:
                cq.Assembly(obj, color=color, name=model_path).save(
                    model_path, tolerance=tolerance, angularTolerance=angular_tolerance)
            except Exception as e:
                print(f"::warning ::Couldn't export {model_path} due to {e}")

        else:  # Default export
            try:
                # noinspection PyTypeChecker
                cq.exporters.export(
                    obj, model_path, fmt, tolerance=tolerance, angularTolerance=angular_tolerance)

                # Fix SVG files forcing a white background
                if fmt == "SVG":
                    with open(model_path, "r") as f:
                        svg = f.read()
                    with open(model_path, "w") as f:
                        f.write(svg.replace(
                            "<g ", '<rect width="99999999%" height="99999999%" fill="white"/><g ', 1))
            except Exception as e:
                print(f"::warning ::Couldn't export {model_path} due to {e}")

        # TODO: Support animations (.gif or .gltf) as a special option with a parametrized time variable


# show() is an alias of show_object() for basic compatibility with ocp-vscode
show = show_object


def debug(*args, **kwargs) -> None:
    """Emulates the cq-editor API to build the models instead."""
    # Force the name to be debug-<name>
    if "name" in kwargs:
        kwargs["name"] = "debug-" + kwargs["name"]
    elif len(args) > 1:
        args = list(args)
        args[1] = "debug-" + args[1]
    else:
        args = list(args)
        args.append(f"debug-{time.time()}")
    # Force the color to be red with transparency
    if "options" in kwargs:
        kwargs["options"]["color"] = (1, 0, 0)
        kwargs["options"]["alpha"] = 0.5
    else:
        kwargs["options"] = {"color": (1, 0, 0), "alpha": 0.5}
    # Call the show_object function
    return show_object(*args, **kwargs)
