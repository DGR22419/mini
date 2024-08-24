document.addEventListener("DOMContentLoaded", function () {
    let questionCounter = document.querySelectorAll('.question-container').length;

    document.querySelector('.add-question').addEventListener('click', function () {
        questionCounter++;
        const questionTemplate = `
            <div class="question-container">
                <h2>Question ${questionCounter}</h2>
                <input type="text" name="questions" placeholder="Enter Question here..." required>
                
                <input type="text" name="options" placeholder="Option A" required>
                <input type="text" name="options" placeholder="Option B" required>
                <input type="text" name="options" placeholder="Option C" required>
                <input type="text" name="options" placeholder="Option D" required>

                <select name="correct_options">
                    <option value="option1">option1</option>
                    <option value="option2">option2</option>
                    <option value="option3">option3</option>
                    <option value="option4">option4</option>
                </select>

                <button type="button" class="delete-question">Delete Question</button>
            </div>
        `;
        document.querySelector('#question-list').insertAdjacentHTML('beforeend', questionTemplate);
        attachDeleteEvents();
        scrollToBottom();
    });

    function attachDeleteEvents() {
        document.querySelectorAll('.delete-question').forEach(button => {
            button.addEventListener('click', function () {
                this.parentElement.remove();
                updateQuestionNumbers();
            });
        });
    }

    function updateQuestionNumbers() {
        document.querySelectorAll('.question-container').forEach((container, index) => {
            const questionNumber = index + 1;
            container.querySelector('h2').textContent = `Question ${questionNumber}`;
            
            // Update input and select names based on the new question number
            container.querySelectorAll('input').forEach((input, idx) => {
                const optionLetter = ['a', 'b', 'c', 'd'][idx];
                input.name = `option_${questionNumber}_${optionLetter}`;
            });

            container.querySelector('select').name = `correct_answer_${questionNumber}`;
        });

        // Update the question counter
        questionCounter = document.querySelectorAll('.question-container').length;
    }

    function scrollToBottom() {
        document.querySelector('.submit-quiz').scrollIntoView({ behavior: 'smooth' });
    }

    attachDeleteEvents();
});
