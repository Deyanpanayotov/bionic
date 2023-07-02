import dash
from dash import dcc
from dash.dependencies import Input, Output
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Binonic Reading"),
        html.Div(
            [
                dcc.Textarea(
                    id="input_text",
                    placeholder="Enter text",
                    style={"width": "400px", "height": "200px"},
                ),
                html.Div(id="boldified", style={"marginLeft": "10px"}),
            ],
            style={"display": "flex", "alignItems": "top"},
        ),
    ]
)
@app.callback(
    Output("boldified", "children"),
    [Input("input_text", "value")]
)
def update_boldified_text(input_text):
    if input_text:
        words = input_text.split()
        boldified_words = []
        for word in words:
            if len(word) >= 5:
                boldified_words.append(html.Span([html.B(word[:3]), word[3:]," "]))
            else:
                if len(word) <= 5 and len(word)>3:
                    boldified_words.append(html.Span([html.B(word[:2]), word[2:], " "]))
                else:
                    boldified_words.append(html.Span([html.B(word[:0]), word[0:]," "]))
        return html.Div(boldified_words)
        
if __name__ == "__main__":
    app.run_server(debug=True)