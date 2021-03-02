import plotly.express as px
from plotly.offline import init_notebook_mode, plot
  
                       
df = px.data.gapminder().query('year == 2007')
fig = px.scatter(
  data_frame = df,
  x = "gdpPercap",
  y = "lifeExp",
  size = "pop",
  color = "continent",
  hover_name = "country",
  log_x = True,
  size_max = 50
)

plot(fig)
