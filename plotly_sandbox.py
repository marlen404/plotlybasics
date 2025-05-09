# Packages plotly.plotly, plotly.graph_objects, plotly.tools
# objects: Figure, layout, data, scatter plot, line chart etc.
import plotly.express as px

# create Figure instance
#fig = px.line(x=[1,2,3], y=[1,2,3], title='Line Chart Example')
#print(fig) # prints Figure object (Plot)
#fig.show() # display figure in browser

# Line Chart
#df = px.data.iris() # use iris dataset
#fig = px.line(df, x="species", y="petal_width", title='Line Chart')
#fig.show()

# Bar Chart
#df = px.data.iris()
#fig = px.bar(df, x="sepal_width", y="sepal_length")
#fig.show()

# Histogram
#df = px.data.iris()
#fig = px.histogram(df, x="sepal_length", y="petal_length")
#fig.show()

# Scatter Plot
#df = px.data.iris()
#fig = px.scatter(df, x="species", y="petal_width")
#fig.show()

# # Bubble Plot
#df = px.data.iris()
#fig = px.scatter(df, x="species", y="petal_width", size="petal_length", color="species")
#fig.show()

# Pie Chart
#df= px.data.tips()
#fig = px.pie(df, values="total_bill", names="day")
#fig.show()

# Box Plot
df = px.data.tips()
fig = px.box(df, x="day", y="total_bill")
fig.show()

# Violin Plot
# Gnatt Chart
# Contour Plot
# Heatmap
# Error Bar
# 3D Line Plot
# 2D Scatter Plot
# 3D Surface Plot

# -- Interactive Plotting --
# Dropdown Menu
# methods to modify charts: restyle, relayout, update, animate

# add buttons
# add sliders and selectors