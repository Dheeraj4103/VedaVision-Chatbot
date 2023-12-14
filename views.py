# myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from main import get_qa_chain
import json

chain = get_qa_chain()

def home(request):
    response = {"message": "This is VedaVision Chatbot"}
    return JsonResponse(response)

@csrf_exempt
def answer_query(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        query = data.get('query')
        try:
            response = chain(query)
        except:
            response = {"history": "", "query": query, "result": "Currently, we didn't find any answer. You can contact an expert for more information."}
        return JsonResponse(response)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"})
