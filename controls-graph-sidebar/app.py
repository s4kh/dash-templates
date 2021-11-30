import dash
import dash_html_components as html
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)
server = app.server  # expose server variable for Procfile

controls = [
    ddk.ControlItem(
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i}
                for i in ['Rear', 'Front', 'Side']
            ],
            multi=True,
            value=['Rear']
        ),
        label='Engine',
    ),
    ddk.ControlItem(
        dcc.Slider(
            min=0,
            max=10,
            marks={
                0: '0',
                3: '3',
                5: '5',
                7.65: '7.65 °F',
                10: '10'
            },
            value=5
        ),
        label='Thrusters',
    ),
    ddk.ControlItem(
        dcc.Input(
            value=50,
            type='number'
        ),
        label='Power',
    )
]

menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='Performance',
        default_open=False,
        children=[
            dcc.Link('Team 1', href=app.get_relative_path('/')),
            dcc.Link('Team 2', href=app.get_relative_path('/')),
        ]
    ),
    dcc.Link('Conditions', href=app.get_relative_path('/')),
    dcc.Link('Historical', href=app.get_relative_path('/')),
    dcc.Link('Portal', href=app.get_relative_path('/')),
])

df = px.data.stocks()

app.layout = ddk.App([

    ddk.Sidebar([
        ddk.Logo(
            src=app.get_asset_url('logo.png'),
        ),
        ddk.Title('Weekly Report'),
        menu
    ], foldable=False),

    ddk.SidebarCompanion([
        ddk.ControlCard(controls, orientation='horizontal'),

        ddk.Card(width=100, children=ddk.Graph(figure=px.line(df, x="date", y=["GOOG", "AAPL"], title='Stowefwefck33 Prices')))
    ])

])


if __name__ == '__main__':
    app.run_server(debug=True)
