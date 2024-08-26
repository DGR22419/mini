document.addEventListener("DOMContentLoaded", function () {
    let questionCounter = document.querySelectorAll('.question-container').length;
    var STATIC_URL = "/static/";


    document.querySelector('.add-question').addEventListener('click', function () {
        // Fetch new question from server
        fetch('/a/add_quiz/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    throw new Error(error.error || 'Failed to load question');
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.questions && data.questions.length > 0) {
                const question = data.questions[0]; // Assuming add_questions contains one question
                questionCounter++;
                const questionTemplate = `
                    <div class="question-container">
                        <h2>Question ${questionCounter}</h2>
                        <input type="text" name="questions" value="${question.question}" placeholder="Enter Question here..." required>
                        
                        <img src="${STATIC_URL}${question.image_loc}" alt="" style="max-width: 500px;">
                        <input type="text" name="img" value="${question.image_loc}" hidden>

                        <input type="text" name="options" value="${question.options[0]}" placeholder="Option A" required>
                        <input type="text" name="options" value="${question.options[1]}" placeholder="Option B" required>
                        <input type="text" name="options" value="${question.options[2]}" placeholder="Option C" required>
                        <input type="text" name="options" value="${question.options[3]}" placeholder="Option D" required>

                        <select name="correct_options">
                            <option value="${question.answer}" >${question.answer}</option>
                        </select>

                        <button type="button" class="delete-question">Delete Question</button>
                    </div>
                `;
                document.querySelector('#question-list').insertAdjacentHTML('beforeend', questionTemplate);
                attachDeleteEvents();
                scrollToBottom();
            } else {
                console.error('Failed to load question:', data.error);
            }
        })
        .catch(error => console.error('Error:', error.message));
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function attachDeleteEvents() {
        document.querySelectorAll('.delete-question').forEach(button => {
            button.removeEventListener('click', handleDelete); // Remove previous event listeners to prevent duplicates
            button.addEventListener('click', handleDelete);
        });
    }

    function handleDelete() {
        this.parentElement.remove(); // Remove the question container
        updateQuestionNumbers(); // Update question numbers after deletion
    }

    function updateQuestionNumbers() {
        document.querySelectorAll('.question-container').forEach((container, index) => {
            const questionNumber = index + 1;
            container.querySelector('h2').textContent = `Question ${questionNumber}`;
            
            container.querySelectorAll('input').forEach((input, idx) => {
                const optionLetter = ['a', 'b', 'c', 'd'][idx];
                input.name = `option_${questionNumber}_${optionLetter}`;
            });

            container.querySelector('select').name = `correct_answer_${questionNumber}`;
        });

        questionCounter = document.querySelectorAll('.question-container').length;
    }

    function scrollToBottom() {
        document.querySelector('.submit-quiz').scrollIntoView({ behavior: 'smooth' });
    }

    attachDeleteEvents(); // Attach delete events to existing questions on page load
});
