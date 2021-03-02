import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd 

# Instanciate the app
app = dash.Dash()

# Build data
options_all = {
	"US": ["New York City", "San Francisco", "Cincinnati"],
	"India": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(options_all)

# Build the app layout
app.layout = html.Div(
	id = "parent",
	children = [
		dcc.Dropdown(
			id = "country-dropdown",
			options = [{"label": i, "value": i} for i in df.columns],
			value = "India"
		),
		html.Br(),
		dcc.Dropdown(id = "states-dropdown"),
		html.Br(),
		html.Div(id = "display-selected-values")
	]
)

# Callbacks
@app.callback(
	Output("states-dropdown", "options"),
	Input("country-dropdown", "value")
)
def set_states_options(selected_country):
	return [{"label": i, "value": i} for i in df["{}".format(selected_country)]]

@app.callback(
	Output("states-dropdown", "value"),
	Input("states-dropdown", "options")
)
def set_states_value(states_options):
	return states_options[0]["value"]

@app.callback(
	Output("display-selected-values", "children"),
	Input("country-dropdown", "value"),
	Input("states-dropdown", "value")
)
def set_display_children(selected_country, selected_state):
	return html.Div("{} is selected state in {}".format(selected_state, selected_country))

# Run the app
if __name__== "__main__":
	app.run_server(debug = True)
