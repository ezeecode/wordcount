from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    # return HttpResponse('Hello! Welcome Home')
    # return render(request, 'home.html', {'hi': 'THIS IS MEE'})
    return render(request, 'home.html')


# def eggs(request):
#     return HttpResponse('EGGGGGSSSS  !!!')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:    # If word exists
            # Increment count by 1
            worddict[word] += 1
        else:
            # Add word to dictionary
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext,
                                          'wordcount': len(wordlist),
                                          'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')
