from django.shortcuts import render
import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as go
import datetime
import random
from sklearn.cluster import KMeans

def analysis(request):

    df = pd.read_csv('./assets/accident2.csv')
    finallist = []
    x = []
    y = []
    y1= []
    y_centers = []
    
    for year in range(2001,2015):
        df1 = df.loc[(df['YEAR'] == year)]

        for i in range(2,14):
            for acc in df1[df1.columns[i]]:
                d = datetime.datetime(year,i-1,random.randint(1,28))
                finallist.append([d,acc])

    for obj in finallist:
        x.append(obj[0])
        y.append(obj[1])
        y1.append([obj[1]])

    dataset = pd.read_csv('./assets/accident2.csv')

    kmeans = KMeans(n_clusters=3 , random_state=0).fit(y1)
    for y_cen in kmeans.cluster_centers_:
        y_centers.append(y_cen[0])
    print(y_centers)
    avg_date = datetime.datetime(2008,6,1)
    x_centers = [avg_date, avg_date, avg_date]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=y, y=x,
        name='values',
        mode='markers',
        marker=dict(color=kmeans.labels_)
    ))

    fig.add_trace(go.Scatter(
        x=y_centers, y=x_centers,
        name='clusters',
        marker_color='rgba(0, 255, 0, .9)',
        marker_size=[80]
    ))

    # Set options common to all traces with fig.update_traces
    fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)
    fig.update_layout(title='Styled Scatter',
                      yaxis_zeroline=False, xaxis_zeroline=False)

    X = dataset.iloc[:, [10,9,1]].values
    # y = dataset.iloc[:, 3].values

    # Using the elbow method to find the optimal number of clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    fig1_a = 'The Elbow Method '
    data = [go.Scatter(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=wcss)]
    fig1 = offline.plot(data, include_plotlyjs=False, output_type='div')
    fig2 = offline.plot(fig, include_plotlyjs=False, output_type='div')
    context = {
          'fig2': fig2,
          'fig1': fig1,
		  'pal' : 12345,
          'fig1_a': fig1_a
         }
    return render(request, 'analysis.html', context)
