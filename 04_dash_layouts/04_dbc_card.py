import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


# Instanciate the app
app = dash.Dash(external_stylesheets = [dbc.themes.FLATLY])


# Define the card content
card_content = [
	dbc.CardHeader("Card Header"),
	dbc.CardBody(
		[
			html.H5(
				"Card Title",
				className = "card-title"
			),
			html.P(
				"This is some card content that we will reuse",
				className = "card-text"
			)
		]
	)
]


# Build the app layout
app.layout = dbc.Container(
	[
		dbc.Row([
			dbc.Col(dbc.Card(card_content, color = "primary", inverse = True)),
			dbc.Col(dbc.Card(card_content, color = "info", inverse = True)),
			dbc.Col(dbc.Card(card_content, color = "secondary", outline = True))
		])
	],
	fluid = True
)

# Run the app
if __name__ == "__main__":
	app.run_server(debug = True)
