from django.shortcuts import render

# Create your views here.
def graph_list(request):
    return render(request, 'graph/template/graph_list.html', {})