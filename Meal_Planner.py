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
import sqlite3
con = sqlite3.connect('meal_planner.db')

# Import data from sqlite to panda
df = pd.read_sql('select * from FoodMenu', con)



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
                id='menu-table',
                columns=[{"name": c, "id": c, "deletable": False, "renamable": False}
                         for c in df.columns], # create all columns at once
                data=df.to_dict('records'),

                editable=True,  # allow user to edit data inside table
                row_deletable=True,  # allow user to delete rows
                sort_action="native",  # sort columns
                sort_mode="single",  # sort single columns
                filter_action="native",  # allow filtering of columns
                page_action='none',  # render all of the data at once. No paging.
                style_table={'height': '350px', 'width': '1450px', 'overflowY': 'auto', 'overflowX': 'scroll'},
                style_cell_conditional=[  # align text columns to center.
                        {
                            'if': {'column_id': c},
                            'textAlign': 'center'
                        } for c in ['Food_Name', 'Category', 'Consume_date']
                    ],
                # style_cell={'textAlign': 'left', 'minWidth': '80px', 'width': '80px', 'maxWidth': '80px'},
                style_data={                # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    }
            ), html.Button('Add Grocery', id='editing-rows1-button', n_clicks=0) ,
])


table_shop=      html.Div([ html.Label("Make Your Groceries Shopping List", style={"color": "blue", "font-weight": "bold"}),
                dash_table.DataTable(
                id='our-table',
                columns=[{'name': 'Product', 'id': 'Product', 'deletable': False, 'renamable': False},
                         {'name': 'Quantity', 'id': 'Quantity', 'deletable': True, 'renamable': True},
                         {'name': 'Notes', 'id': 'Notes', 'deletable': True, 'renamable': True},],
                data=[{'Product': 'Chicken Breast', 'Quantity': '1', 'Notes':'Buy 3 lb only'},
                      {'Product': 'Rice', 'Quantity': '1', },
                      {'Product': 'Pasta', 'Quantity': '7'},
                      {'Product': 'Broccoli', 'Quantity': '8', 'Notes':'Raw'},
                      {'Product': 'Milk', 'Quantity': 'S9'},
                      {'Product': 'Yogurt', 'Quantity': 'S10'},
                      {'Product': 'Beans', 'Quantity': 'S20'},
                      {'Product': 'Fruit', 'Quantity': '1', },
                      {'Product': 'Spaghetti', 'Quantity': '2'},
                      {'Product': 'Water', 'Quantity': '3','Notes':'Refill'},
                      {'Product': 'Soda', 'Quantity': '2'}],
                editable=True,  # allow user to edit data inside table
                row_deletable=True,  # allow user to delete rows
                sort_action="native",  # give user capability to sort columns
                sort_mode="single",  # sort across 'multi' or 'single' columns
                filter_action="native",  # allow filtering of columns
                style_table={'height': '350px', 'width': '400px','overflowY': 'scroll'},
                style_cell={'textAlign': 'left', 'minWidth': '80px', 'width': '80px', 'maxWidth': '80px'},
                style_data={                                             # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    }
                ), html.Button('Add Groceries Shopping Row', id='editing-rows-button', n_clicks=0),
])

# Layout the app
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
    dcc.Graph(id='menu-graph')
])




@app.callback(
    Output('our-table', 'data'),
    [Input('editing-rows-button', 'n_clicks')],
    [State('our-table', 'data'),
     State('our-table', 'columns')],
)
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

@app.callback(
    Output('menu-table', 'data'),
    [Input('editing-rows1-button', 'n_clicks')],
    [State('menu-table', 'data'),
     State('menu-table', 'columns')],
)

def add_row1(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

# Create bar chart
@app.callback(
    Output('menu_graph', 'figure'),
    [Input('menu-table', 'data')])
def display_graph(data):
    df_fig = pd.DataFrame(data)
    fig = px.bar(df_fig, x='Carbohydrates', y='Consume_Date')
    return fig



if __name__ =='__main__':
    app.run_server(port=3000)
