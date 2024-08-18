document.addEventListener("DOMContentLoaded", function () {
  const quizContainer = document.getElementById("quiz");
  const resultContainer = document.getElementById("result");
  const submitButton = document.getElementById("submit-btn");

  // Replace with your JSON data
  const quizData = {
    questions: [
      {
        question: "What is phishing?",
        options: [
          "A. A type of fishing technique",
          "B. A method to catch email spams",
          "C. Attempt to obtain sensitive information by pretending to be trustworthy",
          "D. A form of hacking websites",
        ],
        answer: "C",
      },
      {
        question: "Which of the following is NOT a strong password?",
        options: [
          "A. P@ssw0rd",
          "B. 12345678",
          "C. CorrectHorseBatteryStaple",
          "D. [email protected]#Cyber!",
        ],
        answer: "B",
      },
      {
        question: "What does VPN stand for?",
        options: [
          "A. Virtual Personal Network",
          "B. Virtual Private Network",
          "C. Verified Personal Network",
          "D. Very Private Network",
        ],
        answer: "B",
      },
      {
        question: "Which of the following is a type of malware?",
        options: ["A. SSL", "B. HTTPS", "C. Trojan", "D. IPsec"],
        answer: "C",
      },
      {
        question: "What does 'IoT' stand for in the context of cyber security?",
        options: [
          "A. Internet of Things",
          "B. Internet of Threats",
          "C. Input of Things",
          "D. Input of Threats",
        ],
        answer: "A",
      },
    ],
  };

  function buildQuiz() {
    const output = [];

    quizData.questions.forEach((question, index) => {
      const options = [];
      for (let i = 0; i < question.options.length; i++) {
        options.push(
          `<label>
              <input type="radio" name="question${index}" value="${String.fromCharCode(
            65 + i
          )}">
              ${question.options[i]}
            </label>`
        );
      }

      output.push(
        `<div class="question">${index + 1}. ${question.question}</div>
           <div class="options">${options.join("")}</div>`
      );
    });

    quizContainer.innerHTML = output.join("");
  }

  function showResult() {
    const answerContainers = quizContainer.querySelectorAll(".options");
    let score = 0;

    quizData.questions.forEach((question, index) => {
      const answerContainer = answerContainers[index];
      const selectedOption = answerContainer.querySelector(
        `input[name=question${index}]:checked`
      );

      if (selectedOption) {
        if (selectedOption.value === question.answer) {
          score++;
        }
      }
    });

    resultContainer.innerHTML = `You scored ${score} out of ${quizData.questions.length}`;
  }

  // Display quiz on page load
  buildQuiz();

  // Event listener for submit button
  submitButton.addEventListener("click", showResult);
});
