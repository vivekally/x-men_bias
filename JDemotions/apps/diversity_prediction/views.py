import json
from rest_framework.decorators import api_view
from .helper import JdClassification
from django.shortcuts import render
from .forms import BiasForm


@api_view(["GET", "POST"])
def home(request):
    if request.method == 'POST':
        form = BiasForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_input']
            jd_classifier = JdClassification()
            male_classifier = jd_classifier.male_count(text)
            female_classifier = jd_classifier.female_count(text)
            data = {
                'male_words': male_classifier,
                'female_words': female_classifier
            }
            # print("Male words : ", data['male_words'], ", Female words : ", data['female_words'])
            context = {
                'male_words': json.dumps(data['male_words']),
                'female_words': json.dumps(data['female_words']),
            }
            return render(request, template_name="result_page.html", context=context)
    else:
        form = BiasForm()
        return render(request, 'index.html', {'form': form})


#
# def GetBias(request):
#     template = "result_page.html"
#     try:
#         request_data = request.GET.get("bias_text", None)
#         jd_classifier = JdClassification()
#         male_classifier = jd_classifier.male_count(request_data)
#         female_classifier = jd_classifier.female_count(request_data)
#         data = {
#             'male_words': male_classifier,
#             'female_words': female_classifier
#         }
#     except Exception as  e:
#         response = {
#             'status': 'fail',
#             'data': {},
#             'status_code': 500,
#         }
#         return JsonResponse(response)
#     print("Male words : ", data['male_words'], ", Female words : ", data['female_words'])
#     context = {
#         'male_words': json.dumps(data['male_words']),
#         'female_words': json.dumps(data['female_words']),
#     }
#     return render(request, template_name=template, context=context)


# @api_view(["GET", "POST"])
# def home(request):
#     try:
#         if request.method == 'POST':
#             # create a form instance and populate it with data from the request:
#             form = BIAS_FORM(request.POST)
#             # check whether it's valid:
#             if form.is_valid():
#                 request_data = form.cleaned_data['text_input']
#             # request_data = request.POST.get("text_input", None)
#                 print("\n\n\n\nGet data = ", request_data)
#                 print("\n\n\n\n")
#                 jd_classifier = JdClassification()
#                 male_classifier = jd_classifier.male_count(request_data)
#                 female_classifier = jd_classifier.female_count(request_data)
#                 data = {
#                     'male_words': male_classifier,
#                     'female_words': female_classifier
#                 }
#                 print("Male words : ", data['male_words'], ", Female words : ", data['female_words'])
#                 context = {
#                     'male_words': json.dumps(data['male_words']),
#                     'female_words': json.dumps(data['female_words']),
#                 }
#
#                 return render(request, template_name='result_page.html', context=context)
#
#     except Exception as e:
#         print(e)
#
#     return render(request, template_name="index.html", context={})
