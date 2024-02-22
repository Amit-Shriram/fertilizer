from django.shortcuts import render
from django.http import HttpResponse
# from .fertilizer_data import fertilizer_dic
from .ferti import get_fertilizer_reco
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.POST
        # When you submit an HTML form, regardless of the input type specified in the HTML markup,
        # the data is transmitted to the server as strings in the URL-encoded or multipart-encoded form data. This is the default behavior of HTML forms.
        # So, even though you specify type="number" in your HTML input fields, the browser sends the entered values as strings when the form is submitted.
        crop_name = data.get('cropname')
        n = float(data.get('nitrogen'))
        p = float(data.get('phosphorous'))
        k = float(data.get('potassium'))

        recommend = get_fertilizer_reco(crop_name, n, p, k)
        response_data = {
            'recommendation': recommend
        }
        return JsonResponse(response_data)
        # return render(request, "fertilizer_api/info.html", {
        #     "recommendation": recommend
        # })

    # if request is not post then do this
    # return HttpResponse("Please do POST request to this url.")
    return render(request, "fertilizer_api/index.html")
