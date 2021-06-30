from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    vovels = request.POST.get('vovels', 'off')
    vovelcount = request.POST.get('vovelcount', 'off')
    stringsplit = request.POST.get('stringsplit', 'off')
    
    if removepunc=="on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        
    
    if (fullcaps=='on'):
        analyzed=""
        analyzed=djtext.upper()
        params = {'purpose': 'All Capitals', 'analyzed_text': analyzed}
        djtext=analyzed
        

    if (vovels=='on'):
        v='aeiou'
        analyzed=""
        for char in djtext:
            if char not in v:
                analyzed=analyzed+char
        params = {'purpose': 'Vovels Removed', 'analyzed_text': analyzed}
        djtext=analyzed
        
    
    if (vovelcount=='on'):
        analyzed=""
        v='aeiou'
        for char in djtext:
            if char in v:
                analyzed=analyzed+char
        params = {'purpose': 'Vovel Count', 'analyzed_text': len(analyzed)}
        

    if (stringsplit=='on'):
        analyzed=""
        li=djtext.split(',')
        l2=[]
        for i in li:
            l2.append(i[::-1])
        analyzed= " ".join(l2)
        params = {'purpose': 'String Reverse', 'analyzed_text': analyzed}
    
    if (stringsplit!="on" and vovelcount!="on" and vovels!="on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse('Error')

    return render (request, 'analyze.html', params)
