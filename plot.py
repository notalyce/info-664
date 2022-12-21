# importing modules
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.templates.default = "simple_white"

# csv file name
filename = "release_data_styles.csv"

# filter and clean CSV data

df = pd.read_csv(filename, index_col=0)

df = df[df['style'].str.contains('Techno', na=False)]
df.dropna(inplace = True)
df.drop_duplicates(inplace = True)

# plot releases by format, by year

fig_format_year = px.histogram(df, x="year", color="format")
fig_format_year.update_layout(yaxis_title="Number of Releases", xaxis_title="Year", font_family="monospace")
fig_format_year.write_html("fig_format_year.html")
fig_format_year.show()

# plot releases by style, by year

fig_style_year = px.histogram(df, x="year", color="style")
fig_style_year.update_layout(yaxis_title="Number of Releases", xaxis_title="Year", font_family="monospace")
fig_style_year.write_html("fig_style_year.html")
fig_style_year.show()

# plot releases by style, pie chart

style_count = df['style'].value_counts()
style_count = style_count.to_frame().reset_index()
style_count.set_axis(['style', 'count'],
                    axis=1,inplace=True)
# print(style_count)

fig_style_pie = px.pie(style_count, values='count', names='style', title='Styles')
fig_style_pie.update_layout(font_family="monospace")
fig_style_pie.write_html("fig_style_pie.html")
fig_style_pie.show()

# plot releases by country, pie chart

country_count = df['country'].value_counts()
country_count = country_count.to_frame().reset_index()
country_count.set_axis(['country', 'count'],
                    axis=1,inplace=True)
country_count.loc[country_count['count'] < 250, 'country'] = 'Other countries' # Represent only large countries
print(country_count)

fig_country_pie = px.pie(country_count, values='count', names='country', title='Countries', labels=None)
fig_country_pie.update_layout(font_family="monospace")
fig_country_pie.write_html("fig_country_pie.html")
fig_country_pie.show()