from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html', { "irriswarris" :'hahaha irris warris'})
#dictionary
#def login(request):
        #return HttpResponse('log in successfull')
def count(request):
    alarrajokes = request.GET['alarrajokes']
    #print(alarrajokes)
    wordcount= alarrajokes.split()
    #split the strings into a list of words inside there....wherever there is a sapce

    worddictionary = {}

    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] +=1
            #increase the value of the word by one

        else:
            worddictionary[word]=1
            #add word to the dictionary
    sortedlist=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True )
    return render(request, 'count.html', {'text':alarrajokes, 'count':len(wordcount), 'sortedlist':sortedlist })
    #pass whatever information is stored in variable alarrajokes, count the length of the words stored at variable wordcounr

def about(request):
    return render(request, 'about.html')
