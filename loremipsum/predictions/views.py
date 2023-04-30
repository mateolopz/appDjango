from django.shortcuts import render
from django.template.loader import render_to_string

import requests

#def mostrar(request):
    #return render(request, 'Predictions/consultaBasica.html')

#def post_fastapi_data(request):
    #if request.method == 'POST':
        #payload = {"identificador":0, "review_es":str(request.POST.get('query'))}
        #resp = requests.post('http://localhost:8000/predict', data=payload)
    #return render(request, 'Predictions/consulta.html', {'resultados': resp.text})

def post_fastapi_data(request):
    url = "http://localhost:8000/predict"
    headers = {'Content-type': 'application/json'}
    response = None
    if request.method == 'POST':
        payload = {"identificador":0, "review_es":str(request.POST.get('query'))}
        response = requests.post(url, headers=headers, json=payload)
        return render(request, 'Predictions/consulta.html', {'resultados': response.json()})
    else:
        return render(request, 'Predictions/consultaBasica.html')
#{'resultados': response.json() if response else None}
