document.getElementById("addOption").addEventListener("click", function () {
  // Create a new option container
  const newOptionContainer = document.createElement("div");
  newOptionContainer.classList.add("option-container");

  // Create a new input field for the option
  const newOptionInput = document.createElement("input");
  newOptionInput.type = "text";
  newOptionInput.classList.add("option-input");
  newOptionInput.name = "option";
  newOptionInput.placeholder = "Enter option";
  newOptionInput.required = true;

  // Create a remove button for the option
  const removeButton = document.createElement("button");
  removeButton.type = "button";
  removeButton.classList.add("remove-option");

  let rmBtn = document.getElementsByClassName("remove-option");

  const i = document.createElement("i");

  i.classList.add("fa-solid");
  i.classList.add("fa-trash-can");

  removeButton.append(i);

  removeButton.addEventListener("click", function () {
    newOptionContainer.remove();
  });

  newOptionContainer.appendChild(newOptionInput);
  newOptionContainer.appendChild(removeButton);

  document.getElementById("optionsContainer").appendChild(newOptionContainer);
});

document
  .getElementById("optionsContainer")
  .addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-option")) {
      event.target.parentElement.remove();
    }
  });
