import response
import dash
from dash import html
from dash import dcc
from dash.dependencies import  Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
import pandas_datareader.data as web
import datetime



# mobile layout/ responsiveness
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags = [{'name': 'viewport',
              'content': 'width=device-width, initial-scale=1.0'}]
                )

container_title = dbc.Container([
    # declare column to put on the column component
    dbc.Col(html.H1("Optimum Grocery",
                    className='text-center text-primary mb-4'),
            width=12)
])

        # declare colum to put on the column component
card_monday =   dbc.Card(
            [
                dbc.CardHeader("MONDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Cereal", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Noodle soup", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Roasted Potatoes, Pork Steak",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Grapefruit, Chai", className="card-text")

                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_tuesday=      dbc.Card(
            [
                dbc.CardHeader("TUESDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Pancakes", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Chicken Fried Rice", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Asparagus, Chicken Breast",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Almond, Apples", className="card-text")

                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_wednesday=      dbc.Card(
            [
                dbc.CardHeader("WEDNESDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("English Muffin-Egg", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Chicken Pad Thai", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Dumpling",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Orange", className="card-text")
                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_thursday = dbc.Card(
            [
                dbc.CardHeader("THURSDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Cereal, Egg", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Chicken Quesadilla", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Rice W Lentils, Spinach",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Apple", className="card-text")

                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_friday = dbc.Card(
            [
                dbc.CardHeader("FRIDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Cereal", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Chicken Sandwich", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Chicken drumsticks, Green Beans",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Smoothie, Almond", className="card-text")

                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_saturday=       dbc.Card(
            [
                dbc.CardHeader("SATURDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Pancakes", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Tuna Sandwich", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Rice Pilaf, Palak Paneer",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Fruit Salad", className="card-text")

                    ]
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )
card_sunday=      dbc.Card(
            [
                dbc.CardHeader("SUNDAY"),
                dbc.CardBody(
                    [
                        html.H5("Breakfast", className="card-title"),
                        html.P("Cereal", className="card-text"),
                        html.H5("Lunch", className="card-title"),
                        html.P("Spanish rice", className="card-text"),
                        html.H5("Dinner", className="card-title"),
                        html.P( "Veg Rice W Curry",className="card-text"),
                        html.H5("Snack", className="card-title"),
                        html.P("Hummus, Clementine", className="card-text")

                    ],
                )
            ],
            style={"width": "16rem"}, className="mb-4", color="info", outline=True
        )



table_grocery=          html.Div([ html.Label("Groceries Inventory At Home", style={"color": "blue", "font-weight": "bold","text-align": "justify"}),
                dash_table.DataTable(

                id='our-table1',
                columns=[{'name': 'Groceries', 'id': 'Product', 'deletable': False, 'renamable': False},
                         {'name': 'Purchase Date', 'id': 'Purchase Date', 'type': 'datetime', 'deletable': False, 'renamable': False},
                                   {'name': 'Remaining Qty', 'id': 'Remaining Qty', 'deletable': False, 'renamable': False}],
                data=[{'Product': 'Chicken Breast', 'Purchase Date': '2021-01-07', 'Price': 799, 'Sales': 2813},
                      {'Product': 'Rice', 'Purchase Date': '2021-01-07', 'Price': 900, 'Sales': 5401},
                      {'Product': 'Pasta', 'Purchase Date': '2021-01-07', 'Price': 799, 'Sales': 2513},
                      {'Product': 'Broccoli', 'Purchase Date': '2021-01-07', 'Price': 850, 'Sales': 5401},
                      {'Product': 'Apple', 'Purchase Date': '2021-01-07', 'Price': 900, 'Sales': 6084},
                      {'Product': 'Grapes', 'Purchase Date': '2021-01-07', 'Price': 1000, 'Sales': 7084},
                      {'Product': 'Mixed Greens', 'Purchase Date': '2021-01-07', 'Price': 1200, 'Sales': 9084},
                      {'Product': 'Roma Tomatoes', 'Purchase Date': '2021-01-07', 'Price': 400, 'Sales': 2084}],

                editable=True,  # allow user to edit data inside tabel
                row_deletable=True,  # allow user to delete rows
                sort_action="native",  # give user capability to sort columns
                sort_mode="single",  # sort across 'multi' or 'single' columns
                filter_action="native",  # allow filtering of columns
                page_action='none',  # render all of the data at once. No paging.
                style_table={'height': '350px', 'overflowY': 'auto', 'width': '500px' },
                style_cell={'textAlign': 'left', 'minWidth': '80px', 'width': '80px', 'maxWidth': '80px'},
                style_data={  # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    }
            ), html.Button('Add Grocery', id='editing-rows1-button', n_clicks=0) ,
])


table_shop=      html.Div([ html.Label("Make Your Groceries Shopping List", style={"color": "blue", "font-weight": "bold"}),
                dash_table.DataTable(
                id='our-table',
                columns=[{'name': 'Product', 'id': 'Product', 'deletable': False, 'renamable': False},
                         {'name': 'Version', 'id': 'Version', 'deletable': True, 'renamable': True},
                         {'name': 'Calories', 'id': 'Calories', 'deletable': False, 'renamable': False},],
                data=[{'Product': 'Chicken Breast', 'Version': '6a', 'Price': 799, 'Sales': 2813},
                      {'Product': 'Rice', 'Version': '9', 'Price': 900, 'Sales': 5401},
                      {'Product': 'Pasta', 'Version': '7', 'Price': 799, 'Sales': 2513},
                      {'Product': 'Broccoli', 'Version': '8', 'Price': 850, 'Sales': 5401},
                      {'Product': 'Milk', 'Version': 'S9', 'Price': 900, 'Sales': 6084},
                      {'Product': 'Yogurt', 'Version': 'S10', 'Price': 1000, 'Sales': 7084},
                      {'Product': 'Beans', 'Version': 'S20', 'Price': 1200, 'Sales': 9084},
                      {'Product': 'Fruit', 'Version': '1', 'Price': 400, 'Sales': 2084},
                      {'Product': 'Spaghetti', 'Version': '2', 'Price': 500, 'Sales': 3033},
                      {'Product': 'Soda', 'Version': '3', 'Price': 600, 'Sales': 6000}],
                editable=True,  # allow user to edit data inside table
                row_deletable=True,  # allow user to delete rows
                sort_action="native",  # give user capability to sort columns
                sort_mode="single",  # sort across 'multi' or 'single' columns
                filter_action="native",  # allow filtering of columns
                page_action='native',  # all data is passed to the table up-front.
                page_current=0,        # Current page number
                style_table={'height': '350px', 'overflowY': 'scroll'},
                style_cell={'textAlign': 'left', 'minWidth': '80px', 'width': '80px', 'maxWidth': '80px'},
                style_data={                                             # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    }
                ), html.Button('Add Groceries Shopping Row', id='editing-rows-button', n_clicks=0),
])

# add_column= html.Button('Add Grocery', id='editing-rows-button', n_clicks=0)



app.layout = html.Div([
    dbc.Row([container_title]),
    dbc.Row([dbc.CardGroup([card_monday,card_tuesday, card_wednesday, card_thursday,card_friday,
             card_saturday,card_sunday])
             ]),
    html.Br(),
    html.Br(),
    html.Div([
        dbc.Row([dbc.Col(table_grocery),
                 dbc.Col(table_shop)])
    ]),
    dcc.Graph(id='groceries-graph')
])




@app.callback(
    Output('our-table', 'data'),
    [Input('editing-rows-button', 'n_clicks')],
    [State('our-table', 'data'),
     State('our-table', 'columns')],
)
def add_row(n_clicks, rows, columns):
    # print(rows)
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    # print(rows)
    return rows

@app.callback(
    Output('our-table1', 'data'),
    [Input('editing-rows1-button', 'n_clicks')],
    [State('our-table1', 'data'),
     State('our-table1', 'columns')],
)
def add_row1(n_clicks, rows, columns):
    # print(rows)
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    # print(rows)
    return rows


if __name__ =='__main__':
    app.run_server(debug =True, port=3000)
