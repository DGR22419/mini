let questionCount = 1;

function addOption(button) {
    const questionBlock = button.closest('.question-block');
    const optionBlock = document.createElement('div');
    optionBlock.className = 'option-block';
    optionBlock.innerHTML = `
        <input type="text" placeholder="Option" name="option">
        <button type="button" class="delete-option" onclick="deleteOption(this)">&#128465;</button>
    `;
    questionBlock.insertBefore(optionBlock, button.parentElement);
}

function deleteOption(button) {
    const optionBlock = button.parentElement;
    optionBlock.remove();
}

function addQuestion() {
    questionCount++;
    const questionContainer = document.getElementById('questionContainer');
    const questionBlock = document.createElement('div');
    questionBlock.className = 'question-block';
    questionBlock.setAttribute('data-question', questionCount);
    questionBlock.innerHTML = `
        <h3>Question ${questionCount}</h3>
        <textarea placeholder="Enter Question here..." name="question"></textarea>
        <div class="option-block">
            <input type="text" placeholder="Option A" name="option">
            <button type="button" class="delete-option" onclick="deleteOption(this)">&#128465;</button>
        </div>
        <div class="option-block">
            <input type="text" placeholder="Option B" name="option">
            <button type="button" class="delete-option" onclick="deleteOption(this)">&#128465;</button>
        </div>
        <div class="option-block">
            <input type="text" placeholder="Option C" name="option">
            <button type="button" class="delete-option" onclick="deleteOption(this)">&#128465;</button>
        </div>
        <div class="option-block">
            <input type="text" placeholder="Option D" name="option">
            <button type="button" class="delete-option" onclick="deleteOption(this)">&#128465;</button>
        </div>
        <div class="control-buttons">
            <select name="answer">
                <option selected disabled>Select Answer</option>
                <option value="A">Option A</option>
                <option value="B">Option B</option>
                <option value="C">Option C</option>
                <option value="D">Option D</option>
            </select>
            <button type="button" onclick="addOption(this)">Add Option</button>
            <button type="button" onclick="deleteQuestion(this)" class="delete-question">Delete Question</button>
        </div>
    `;
    questionContainer.appendChild(questionBlock);
}

function deleteQuestion(button) {
    const questionBlock = button.closest('.question-block');
    questionBlock.remove();
    questionCount--;
}

document.getElementById('quizForm').onsubmit = function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const quizData = [];

    // Iterate through questions
    document.querySelectorAll('.question-block').forEach((questionBlock, index) => {
        const questionText = questionBlock.querySelector('textarea').value;
        const options = Array.from(questionBlock.querySelectorAll('input[name="option"]')).map(input => input.value);
        const answer = questionBlock.querySelector('select[name="answer"]').value;

        quizData.push({
            question: questionText,
            options: options,
            answer: answer
        });
    });

    // Convert quizData to JSON
    const jsonData = JSON.stringify(quizData);

    // Send the JSON data via POST request
    fetch('/submit-quiz/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Quiz submitted successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Failed to submit quiz.');
    });
};
