import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div([
	dcc.Input(id = "input-1-state", type = "text", value = "Montréal"),
	dcc.Input(id = "input-2-state", type = "text", value = "Canada"),
	html.Button(id = "submit-button-state", n_clicks = 0, children = "Submit"),
	html.Div(id = "output-state")
])

# Update output
@app.callback(
	Output(component_id = "output-state", component_property = "children"),
	Input(component_id = "submit-button-state", component_property = "n_clicks"),
	State(component_id = "input-1-state", component_property = "value"),
	State(component_id = "input-2-state", component_property = "value")
)
def update_output(n_clicks, input1, input2):
	txt = """
	The button has been pressed {0} times
   Input 1 is {1}
   and Input 2 is {2}
	""".format(n_clicks,input1, input2)
	# Return the text
	return txt

# Run the app
if __name__== "__main__":
	app.run_server(debug = True)

