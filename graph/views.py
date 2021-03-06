from django.shortcuts import render

import django
import matplotlib
import random
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'graph/graph_list.html', {})

def graph_list(request):
    return render(request, 'graph/graph_list.html', {})

def tableau(request):
    return render(request, 'graph/tableau.html', {})

def simple(request):

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)

    return response
