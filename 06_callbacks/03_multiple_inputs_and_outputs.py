import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import numpy as np

# Get data
df = px.data.gapminder()

# Instanciate the app
app = dash.Dash()

# Define the layout
app.layout = html.Div(
	id = "parent",
	children = [
		html.Div(
			id = "slider-div",
			children = [
				dcc.Slider(
					id = "year-slider",
					min = df["year"].min(),
					max = df["year"].max(),
					value = df["year"].min(),
					marks = {str(year): str(year) for year in df["year"].unique()},
					step = None
				)
			],
			style = {
				"width": "50%",
				"display": "inline-block"
			}
		),
		html.Div(
			id = "dropdown-div",
			children = [
				dcc.Dropdown(
					id = "continent-dropdown",
					options = [{"label": i, "value": i} for i in np.append(["All"], df["continent"].unique())],
					value = "All"
				)
			],
			style = {
				"width": "50%",
				"display": "inline-block"
			}
		),
		html.Div(id = "filters-selected", style = {"textAlign": "center"}),
		dcc.Graph(id = "scatter-plot")
	]
)

# Update the plot
@app.callback(
	Output("filters-selected", "children"),
	Output("scatter-plot", "figure"),
	Input("year-slider", "value"),
	Input("continent-dropdown", "value")
)
def graph_update(slider_value, dropdown_value):
	# Filter the data
	if dropdown_value == "All":
		filtered_df = df.loc[(df["year"] == slider_value)]
	else:
		filtered_df = df.loc[(df["year"] == slider_value) & (df["continent"] == dropdown_value)]
	# Build the fig	
	fig = px.scatter(
		filtered_df,
		x = "gdpPercap",
		y = "lifeExp",
		size = "pop",
		color = "continent",
		hover_name = "country",
		log_x = True,
		size_max = 55,
		range_x = [100, 100000],
		range_y = [25, 90]
	)
	# Return the fig
	return html.Div("Selected year {} and selected continent {}".format(slider_value, dropdown_value)), fig
    
# Run the app
if __name__== "__main__":
	app.run_server()

