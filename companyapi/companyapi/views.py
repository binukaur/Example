from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page requested")
    friends = [
        'Binu',
        'Anu',
        'Yashu'
    ]
    return JsonResponse(friends,safe = False)