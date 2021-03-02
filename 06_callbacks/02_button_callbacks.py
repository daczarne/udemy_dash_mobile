import dash
import dash_html_components as html
from dash.dependencies import Input, Output

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div(
	id = "parent",
	children = [
		html.Button(
			id = "html-button",
			children = "Click the button!",
			n_clicks = 0
		),
		html.Br(),
		html.Div(id = "output-text")
	]
)

# Update output text
@app.callback(
	Output(component_id = "output-text", component_property = "children"),
	Input(component_id = "html-button", component_property = "n_clicks")
)
def button_update(value):
	return html.Div(str(value) + " clicks!")

# Run the app
if __name__ == "__main__":
	app.run_server(debug = False)
