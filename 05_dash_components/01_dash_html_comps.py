import dash
import dash_html_components as html


# Instanciate the app
app = dash.Dash()


# Define the layout
app.layout = html.Div(
	id = "parent",
	children = [
		html.H1(
			id = "H1",
			children = "Hello! This is an H1 tag",
			style = {"textAlign": "center"}
		),
		html.H2(
			id = "H2",
			children = "Hello! This is an H2 tag",
			style = {"textAlign": "center"}
		),
		html.P(
			id = "para",
			children = "This is a paragraph tag",
			style = {"textAlign": "center"}
		),
		html.Div(
			id = "link_div",
			children = [
				html.A(
					id = "link",
					children = "Udemy link",
					href = "https://www.udemy.com",
					style = {"fontSize": 30}
				)
			],
			style = {"textAlign": "center"}
		),
		html.Br(),
		html.Img(
			id = "image",
			src = "https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png",
			height = "50px"
		),
		html.Marquee(
			id = "marquee",
			children = "Hello! This can be used to show some notifications"
		)
	]
)


# Run the app
if __name__ == "__main__":
	app.run_server()
