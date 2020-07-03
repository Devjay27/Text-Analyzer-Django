from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'txt.html')


def analyze(request):
    dtext = request.GET.get('text', 'default')
    removepunctuation = request.GET.get('removepunctuations', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    lowercase = request.GET.get('lowercase', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    length = request.GET.get('length', 'off')
    print(removepunctuation)
    print(dtext)
    if removepunctuation == 'on':
        # analyzed = dtext
        punctuations = ''' \!()-[]{};:'"<>,./?@#$%^&*_~ '''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        para = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', para)

    elif uppercase == "on":
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()

        para = {'purpose': 'Changed to UPPER CASE', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', para)

    elif lowercase == "on":
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.lower()

        para = {'purpose': 'Changed to LOWER CASE', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', para)

    elif extraspaceremover == "on":
        analyzed = ""
        for indx, char in enumerate(dtext):
            if not(dtext[indx] == " " and dtext[indx+1] == " "):
                analyzed = analyzed + char

        para = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', para)

    elif length == "on":
        analyzed = len(dtext)

        para = {'purpose': 'Count', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', para)

    else:
        return HttpResponse('Error')
