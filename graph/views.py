from django.shortcuts import render

# Create your views here.
def graph_list(request):
    return render(request, 'graph/graph_list.html', {})