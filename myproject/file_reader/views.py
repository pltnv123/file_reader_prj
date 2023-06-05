from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict


def wordcount(request):
    if request.method == 'POST':
        word_counts = defaultdict(int)
        uploaded_file = request.FILES['document']
        for line in uploaded_file:
            word = ''
            for char in line.decode('utf-8'):
                if char.isalpha():
                    word += char.lower()
                elif word:
                    word_counts[word] += 1
                    word = ''
            if word:
                word_counts[word] += 1
        word = request.POST.get('word', '').lower()
        count = word_counts.get(word, 0)
        return render(request, 'wordcount.html', {'count': count})
    return render(request, 'wordcount.html')


def clear_memory(request):
    if request.method == 'POST':
        request.session.clear()
        return HttpResponse("Память очищена")
    return render(request, 'clear_memory.html')