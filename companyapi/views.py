from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested")
    friends=[
        "ankit",
        "rahul",
        "Ram"
    ]
    # return HttpResponse("This is home page .")
    return JsonResponse(friends,safe=False)