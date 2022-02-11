import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from user_profile.models import UserProfile
from .models import Calculations


def index(request):
    if request.user.is_authenticated:
        obj = UserProfile.objects.get(profile_user=request.user)
        calculations = Calculations.objects.filter(owner=obj)
        return render(request, 'input.html', {'calculations': calculations})
    else:
        return HttpResponse("You are not authorized to view this page !")

def calci(request):
    if request.user.is_authenticated:
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        opr = request.GET.get('opr')
        check = False
        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            if opr == 'ADD':
                opr = '+'
                res = a + b
                check = True
            elif opr == 'SUB':
                opr = '-'
                res = a - b
                check = True
            elif opr == 'DIV':
                opr = '/'
                if b != 0:
                    res = a / b
                    check = True
                else:
                    res = "For division denominator should not be zero !"
            else:
                opr = '*'
                res = a * b
                check = True
            if check:
                value = str(a)+" "+opr+" "+str(b) + "=" + str(res)
                try:
                    obj = UserProfile.objects.get(profile_user=request.user)
                    calc = Calculations.objects.create(owner=obj, entries=value)

                except UserProfile.DoesNotExist:
                    obj = UserProfile.objects.create(profile_user=request.user)
                    calc = Calculations.objects.create(owner=obj, entries=value)
            obj = UserProfile.objects.get(profile_user=request.user)
            calculations = Calculations.objects.filter(owner=obj).values()
            return JsonResponse({"result": res, "calculations": list(calculations)})
        else:
            res = "Only digits are allowed, no alphabets no special characters or blank"
            return JsonResponse({"result": res})
    else:
        return HttpResponse("You are not authorized to view this page !")
