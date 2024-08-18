const btn = document.querySelector("#startBtn");
const div = document.querySelector(".start-quiz-popup");
const closeBtn = document.querySelector(".fa-xmark");

const container = document.querySelector(".container");

btn.addEventListener("click", () => {
  div.classList.add("active");
  container.classList.add("container-active");
});

closeBtn.addEventListener("click", () => {
  div.classList.remove("active");
  container.classList.remove("container-active");
});

const phoneMenuBtn = document.querySelector("#mobileMenu");
const phoneMenuDiv = document.querySelector("#mobileMenuDiv");

let x = 0;

phoneMenuBtn.addEventListener("click", () => {
  if (x == 1) {
    mobileMenuDiv.style.display = "none";
    x = 0;
  } else {
    mobileMenuDiv.style.display = "block";
    x = 1;
  }
});
