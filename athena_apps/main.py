# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output,State

"""
    user will give a phrase and press enter
    
    then we will  do a background callback:
        render the place of the letter then calls a __function__
        to slowy reveale each tag one by one
    
"""


app = Dash(__name__)

app.layout = html.Div([

    html.Div([ # user type in phrase
        dcc.Input(id="txt1", type="text", placeholder="type a phrase")
    ]),

    html.Div([ 
        html.P("Word Count: ", id = "output"),
        html.Ul(id = "letters", style={"list-style-type" : "none"},
            children=[]
        ),
    ]),
])
    
@app.callback(
    Output("letters", "children"), #list li in the ul
    #Output("output", "children"), # number of words
    [Input("txt1", "value")], # the phrase being given
    [State("letters","children")]
)
def update(phrase,old):
    tmp = [] #[my name is martell]
    for x in phrase.split():
        tmp.append(x)
    
    
    return [old + html.Li([tmp[word]]) for word in range(0,len(tmp))]
    
    
    #return old + [html.Li( [tmp[0]] ) for x in range(0,len(tmp))]

"""

instead:
    have the user type in the phrase
        * display the user phrase

    have a button that loops through the phrase
        * for each letter and space make
            a html.LI([]) 

"""

if __name__ == "__main__":
    app.run_server(debug=True)
