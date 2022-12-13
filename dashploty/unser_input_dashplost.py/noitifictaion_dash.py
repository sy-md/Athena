from dash import Dash, dcc, html, Input, Output, dash_table

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Store(id="notification-permission"),
        html.Button("Notify", id="notify-btn"),
        html.Div(id="notification-output"),
    ]
)


app.clientside_callback(
    """
    function() {
        return navigator.permissions.query({name:'notifications'})
    }
    """,
    Output("notification-permission", "data"),
    Input("notify-btn", "n_clicks"),
    prevent_initial_call=True,
)

app.clientside_callback(
    """
    function(result) {
        if (result.state == 'granted') {
            new Notification("Dash notification", { body: "Notification already granted!"});
            return null;
        } else if (result.state == 'prompt') {
            return new Promise((resolve, reject) => {
                Notification.requestPermission().then(res => {
                    if (res == 'granted') {
                        new Notification("Dash notification", { body: "Notification granted!"});
                        resolve();
                    } else {
                        reject(`Permission not granted: ${res}`)
                    }
                })
            });
        } else {
            return result.state;
        }
    }
    """,
    Output("notification-output", "children"),
    Input("notification-permission", "data"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
