from typing import Any, Union

from dash import dcc, html
from dash.development.base_component import Component


def Spinner(
    children: Any = None,
    variant: str = "light",
):
    # Raise exceptions if arguments do not match required data types or values
    if not isinstance(variant, str):
        raise TypeError("variant must be a string")
    if variant not in ["light", "dark"]:
        raise ValueError("variant must be a string equal to either 'light' or 'dark'")

    return dcc.Loading(
        children=children,
        overlay_style={
            "visibility": "visible",
            "opacity": 0.3,
            "backgroundColor": "white" if variant == "light" else "black",
            "filter": "blur(1px)",
        },
        custom_spinner=html.Div(
            className="sdc-spinner" if variant == "light" else "sdc-spinner-dark"
        ),
    )
