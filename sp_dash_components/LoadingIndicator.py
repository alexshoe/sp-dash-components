from typing import Any, Union

from dash import dcc, html
from dash.development.base_component import Component


def LoadingIndicator(
    children: Any = None,
    loading_bar: bool = True,
    description: str = "Loading is delayed for some reason",
    variant: str = "light",
):
    # Raise exceptions if arguments do not match required data types or values
    if not isinstance(loading_bar, bool):
        raise TypeError("loading_bar must be a boolean value")
    if not isinstance(description, str):
        raise TypeError("description must be a string")
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
            [
                html.Div(
                    description,
                    className=(
                        "sdc-loading-indicator-text"
                        if variant == "light"
                        else "sdc-loading-indicator-text-dark"
                    ),
                ),
                html.Div(className="sdc-loading-bar") if loading_bar else None,
                (
                    html.Div(
                        "Loading...",
                        className=(
                            "sdc-loading-indicator-text"
                            if variant == "light"
                            else "sdc-loading-indicator-text-dark"
                        ),
                    )
                    if loading_bar
                    else None
                ),
            ],
            className=(
                "sdc-loading-indicator"
                if variant == "light"
                else "sdc-loading-indicator-dark"
            ),
        ),
        parent_style={"height": "100%", "width": " 100%"},
    )
