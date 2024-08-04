# S&P Dash Components

S&P Dash Components is a custom Dash components library built for S&P Global by the Plotly Professional Services Team.

## Installation

```bash
pip install sp-dash-components
```

## Quickstart

```python
from datetime import date

import dash
from dash import Dash, Input, Output, callback, html
from dash.exceptions import PreventUpdate

import sp_dash_components as sdc

app = Dash(__name__)

app.layout = html.Div(

)


if __name__ == "__main__":
    app.run_server(debug=True)
```
