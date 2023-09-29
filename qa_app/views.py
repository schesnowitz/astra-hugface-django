from django.shortcuts import render
from uuid import uuid4
from .models import CnnVectors, Answers
from django.views.decorators.http import require_POST
from .question_answering import run_retrieval_qa_pipeline


def index(request):
    articles = CnnVectors.objects.all()
    context = {'articles' : articles}
    return render(request=request, template_name="index.html", context=context)


@require_POST
def submit_question(request):
    prompt = request.POST.get("prompt")
    instruction = request.POST.get("qa-instructions")
    answer = run_retrieval_qa_pipeline(prompt, instruction)
    Answers.objects.create(row_id=uuid4(), question=prompt, answer=answer)
    context = { 'question' :  prompt, 'answer' : answer}
    return render(request=request, template_name="answer.html", context=context)