document.addEventListener("DOMContentLoaded", () => {
  const questionsContainer = document.getElementById("questionsContainer");
  const addQuestionButton = document.getElementById("addQuestion");

  let questionCount = 0;

  function createQuestion() {
    questionCount++;

    const questionDiv = document.createElement("div");
    questionDiv.className = "question";
    questionDiv.innerHTML = `
           <h3 class="question-label">Question ${questionCount}</h3>
           <textarea placeholder="Enter Question here..." required></textarea>
           <div class="options-container">
               <div class="option-group">
                   <input type="text" placeholder="Option A" required>
                   <button type="button" class="delete-option"><i class="fa-solid fa-trash-can"></i></button>
               </div>
               <div class="option-group">
                   <input type="text" placeholder="Option B" required>
                   <button type="button" class="delete-option"><i class="fa-solid fa-trash-can"></i></button>
               </div>
               <div class="option-group">
                   <input type="text" placeholder="Option C">
                   <button type="button" class="delete-option"><i class="fa-solid fa-trash-can"></i></button>
               </div>
               <div class="option-group">
                   <input type="text" placeholder="Option D">
                   <button type="button" class="delete-option"><i class="fa-solid fa-trash-can"></i></button>
               </div>
           </div>
         <select>
            <option>Select Answer</option>
            <option>A</option>
            <option>B</option>
            <option>C</option>
            <option>D</option>
         </select>

           <button type="button" class="add-option">Add Option</button>
           <button type="button" class="delete-question">Delete Question</button>
       `;

    const addOptionButton = questionDiv.querySelector(".add-option");
    const deleteQuestionButton = questionDiv.querySelector(".delete-question");

    // Handle adding options
    addOptionButton.addEventListener("click", () => {
      const optionsContainer = questionDiv.querySelector(".options-container");
      const optionGroups = optionsContainer.querySelectorAll(".option-group");

      if (optionGroups.length < 4) {
        const newOption = document.createElement("div");
        newOption.className = "option-group";
        newOption.innerHTML = `
                   <input type="text" placeholder="Option ${String.fromCharCode(
                     65 + optionGroups.length
                   )}">
                   <button type="button" class="delete-option"><i class="fa-solid fa-trash-can"></i></button>
               `;
        optionsContainer.appendChild(newOption);

        // Attach event listener to the new delete button
        newOption
          .querySelector(".delete-option")
          .addEventListener("click", () => {
            newOption.remove();
          });
      } else {
        alert("YOU CAN ADD ONLY 4 OPTIONS.");
      }
    });

    // Handle deleting options
    questionDiv.querySelectorAll(".delete-option").forEach((button) => {
      button.addEventListener("click", () => {
        const optionGroup = button.parentElement;
        optionGroup.remove();
      });
    });

    // Handle deleting questions
    deleteQuestionButton.addEventListener("click", () => {
      if (confirm("Are you sure you want to delete this question?")) {
        questionDiv.remove();
        questionCount--;
        updateQuestionNumbers();
      }
    });

    questionsContainer.appendChild(questionDiv);
  }

  function updateQuestionNumbers() {
    const questions = questionsContainer.querySelectorAll(".question");
    questions.forEach((question, index) => {
      question.querySelector("h3").textContent = `Question ${index + 1}`;
    });
  }

  addQuestionButton.addEventListener("click", createQuestion);

  // Add the first question initially
  createQuestion();
});

// ==============================================================================

// document.addEventListener("DOMContentLoaded", () => {
//   const questionsContainer = document.getElementById("questionsContainer");
//   const addQuestionButton = document.getElementById("addQuestion");

//   let questionCount = 0;

//   function createQuestion() {
//     questionCount++;

//     const questionDiv = document.createElement("div");
//     questionDiv.className = "question";
//     questionDiv.innerHTML = `
//            <h3>Question ${questionCount}</h3>
//            <textarea placeholder="Enter your question here..." required></textarea>
//            <div class="options-container">
//                <input type="text" placeholder="Option A" required>
//                <input type="text" placeholder="Option B" required>
//                <input type="text" placeholder="Option C">
//                <input type="text" placeholder="Option D">
//            </div>
//            <input type="text" placeholder="Correct Answer (A, B, C, or D)" required>
//            <button type="button" class="add-option">Add Option</button>
//            <button type="button" class="delete-question">Delete Question</button>
//        `;

//     const addOptionButton = questionDiv.querySelector(".add-option");
//     const deleteQuestionButton = questionDiv.querySelector(".delete-question");

//     addOptionButton.addEventListener("click", () => {
//       const optionsContainer = questionDiv.querySelector(".options-container");
//       const currentOptions = optionsContainer.querySelectorAll("input").length;

//       if (currentOptions < 4) {
//         const newOption = document.createElement("input");
//         newOption.type = "text";
//         newOption.placeholder = `Option ${String.fromCharCode(
//           65 + currentOptions
//         )}`;
//         optionsContainer.appendChild(newOption);
//       } else {
//         alert("Maximum 4 options allowed.");
//       }
//     });

//     deleteQuestionButton.addEventListener("click", () => {
//       if (confirm("Are you sure you want to delete this question?")) {
//         questionDiv.remove();
//         questionCount--;
//         updateQuestionNumbers();
//       }
//     });

//     questionsContainer.appendChild(questionDiv);
//   }

//   function updateQuestionNumbers() {
//     const questions = questionsContainer.querySelectorAll(".question");
//     questions.forEach((question, index) => {
//       question.querySelector("h3").textContent = `Question ${index + 1}`;
//     });
//   }

//   addQuestionButton.addEventListener("click", createQuestion);

//   // Add the first question initially
//   createQuestion();
// });
