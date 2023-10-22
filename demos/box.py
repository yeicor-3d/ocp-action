import cadquery as cq

show(
    cq.Workplane("XY").box(1, 2, 3),
    "simple_box", {"color": "green", "alpha": 0.5},
)
