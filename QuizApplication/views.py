from django.shortcuts import render

# Create your views here.
from QuizApplication.models import Question, Option, Quiz, Result

def calculateScore(quizAnsList,name):
    Options = Option.objects.filter(correct_answer = True)
    OptionsWrong = Option.objects.filter(correct_answer= False)

    score = 0
    total = 0
    wrongAnswered = []
    for quiz in quizAnsList:
        total = total + 1
        quesId = quiz['question']
        sel_answer = quiz['sel_answer']
        cor_answer = list(filter(lambda opt : opt.question_id_id == quesId, Options))
        if str(cor_answer[0].option_id) == sel_answer:
            score = score + 1
        else:
           wrongQues = dict()
           wrongQues['question'] = list(Question.objects.filter(question_id=quesId))[0].question_value
           wrongQues['correct_answer'] = cor_answer[0].option_value
           wrongQues['your_answer'] = list(filter(lambda opt : str(opt.option_id) == sel_answer, OptionsWrong))[0].option_value
           wrongQues['id'] = quesId
           wrongAnswered.append(wrongQues)

    percentage = float((score/total)*100)
    res_obj = Result.objects.create(user_name=name, score=score, percentage=percentage)

    return score,total,wrongAnswered


def submitAnswer(request):
    noOfQues = len(request.POST) - 2
    quizAnsList = []
    for i in range(1,noOfQues,1):
        quizQues = dict()
        quesNo = i
        selAns = request.POST['ques'+str(quesNo)]
        quizQues['question'] = quesNo
        quizQues['sel_answer'] = selAns
        quizAnsList.append(quizQues)
    score,total,wrongAnswered = calculateScore(quizAnsList,request.POST['stuName'])

    return render(request, "QuizResult.html", {"Name":request.POST['stuName'],"Score":score,"Total":total,"WrongAnswered":wrongAnswered})

def getAddQuiz(request):
    return render(request, "AddQuiz.html")

def home(request):
    Questions = Question.objects.all()
    Options = Option.objects.all()

    quizList = []
    for q in Questions:
        ques_id = q.question_id
        question = Question()
        quiz = Quiz()

        question.question_id = ques_id
        question.question_value = q.question_value

        quiz.question = question

        options = list(filter(lambda opt : opt.question_id_id == ques_id, Options))
        quiz.options = options
        quizList.append(quiz)

    return render(request, "QuizHome.html",{'Quiz':quizList})

def addQuiz(request):
    noOfQues = int(((len(request.POST) - 2)/3) + 1)
    for q in range(1,noOfQues,1):
        question = request.POST['question'+str(q)]
        answer = request.POST['answer'+str(q)]
        optionStr = str(request.POST['option'+str(q)])
        options = optionStr.split(',')

        quesionObj = Question.objects.create(question_value=question)
        for opt in options:
            if opt == str(answer):
                Option.objects.create(option_value=opt, correct_answer=True, question_id_id=quesionObj.question_id)
            else:
                Option.objects.create(option_value=opt, correct_answer=False, question_id_id=quesionObj.question_id)

    return render(request, "AddQuizSuccess.html", {"message" : True})
