quesCounter = 0;
function addQuestion(){
    var questionDiv = document.getElementById('quizQuesRef').cloneNode(true);
    quesCounter++;
    questionDiv.id = "quizQues"+quesCounter;
    questionDiv.style="display:block";
    quesEle = questionDiv.querySelector('#question');
    quesEle.name = "question"+quesCounter;
    quesEle.id = "question"+quesCounter;
    optionEle = questionDiv.querySelector('#option');
    optionEle.name = "option"+quesCounter;
    optionEle.id = "option"+quesCounter;
    ansEle = questionDiv.querySelector('#answer');
    ansEle.id = "answer"+quesCounter;
    ansEle.name = "answer"+quesCounter;
    var quizDiv = document.getElementById('Quiz');
    quizDiv.appendChild(questionDiv);
}