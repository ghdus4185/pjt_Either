from django.shortcuts import render, redirect
from .models import Qu, An
import random as rand
# Create your views here.
def index(request):
    questions = Qu.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        choice1 = request.POST.get("choice1")
        choice2 = request.POST.get("choice2")
        image_url1 = request.POST.get("image_url1")
        image_url2 = request.POST.get("image_url2")
        Qu.objects.create(
            title = title,
            choice1 = choice1,
            choice2 = choice2,
            p1 = 0,
            p2 = 0,
            image_url1 = image_url1,
            image_url2 = image_url2,
        )
        return redirect('question:index')

    else:
        return render(request, 'form.html')

def detail(request, id):
    question = Qu.objects.get(id=id)
    context = {
        "question" : question
    }
    return render(request, "detail.html", context)

def delete(request, id):
    question = Qu.objects.get(id=id)
    question.delete()
    return redirect('question:index')

def update1(request, id):
    question = Qu.objects.get(id=id)
    print(question.p1)
    question.p1 += 1
    question.save()
    return redirect('question:detail', id)

def update2(request, id):
    question = Qu.objects.get(id=id)
    question.p2 += 1
    question.save()
    return redirect('question:detail', id)

def edit(request, id):
    question = Qu.objects.get(id=id)
    if request.method == "POST": 
        question.title = request.POST.get("title")
        question.choice1 = request.POST.get("choice1")
        question.choice2 = request.POST.get("choice2")
        question.image_url1 = request.POST.get("image_url1")
        question.image_url2 = request.POST.get("image_url2")
        question.save()

        return redirect('question:detail', id)
    else:
        context = {
            'question': question
        }
        return render(request, 'form.html', context)

def answer_create(request, question_id):
    if request.method == "POST":
        content = request.POST.get('content')
        question = Qu.objects.get(id=question_id)

        An.objects.create(content=content, question=question)

        return redirect('question:detail', question_id)
    else:
        pass

def answer_delete(request, question_id, answer_id):
    answer = An.objects.get(id=answer_id)
    answer.delete()
    return redirect('question:detail', question_id)

def random(request):
    questions=Qu.objects.all()
    R = []
    for question in questions:
        R.append(question.id)
    res = rand.choice(R)
    return redirect('question:detail', res)

def search(request):    
    S = request.GET.get('search')
    questions=Qu.objects.all()
    context={
        "S" : S,
        "questions":questions
    }
    return render(request, 'search.html', context)