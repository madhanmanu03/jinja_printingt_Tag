from django.shortcuts import render

# Create your views here.
def data_render(request):
    data="madhan arun ramani barath "
    d={'ass':data}
    return render(request,'data_render.html',context=d)