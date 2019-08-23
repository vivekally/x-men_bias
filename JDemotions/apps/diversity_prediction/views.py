from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helper import JdClassification


@api_view(["POST"])
def GetBias(request):
    try:
        request_data = request.data
        male_classifier = JdClassification.male_count(request_data)
        female_classifier = JdClassification.female_count(request_data)
        data = {
            'male_words': male_classifier,
            'female_words': female_classifier
        }
        response = {
            'status': 'success',
            'data': data,
            'status_code': 200,
        }
    except:
        response = {
            'status': 'fail',
            'data': {},
            'status_code': 500,
        }
    return Response(response)
