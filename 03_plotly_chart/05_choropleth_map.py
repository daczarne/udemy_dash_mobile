import plotly.express as px
from plotly.offline import init_notebook_mode, plot

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth(
  data_frame = df,
  geojson = geojson,
  locations = "district",
  featureidkey = "properties.district",
  projection = "mercator",
  color = "Bergeron"
)

fig.update_geos(
  fitbounds = "locations",
  visible = False
)

df = px.data.gapminder().query("year==2007")

fig = px.choropleth(
  data_frame = df,
  locations = "iso_alpha",
  color = "lifeExp",
  hover_name = "country",
  projection = "orthographic",
  color_continuous_scale = px.colors.sequential.Plasma
)

plot(fig)
