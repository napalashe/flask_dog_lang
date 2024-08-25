document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const selectionBoxes = document.querySelectorAll(".selection-box");
  const resultDiv = document.querySelector(".result");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    selectionBoxes.forEach((box) => {
      box.classList.add("fade-out");
    });

    setTimeout(function () {
      form.submit();
    }, 500);
  });

  if (resultDiv) {
    setTimeout(function () {
      resultDiv.classList.add("fade-in");
    }, 500); // Start fading in after a brief delay

    resultDiv.style.transition = "opacity 5s ease";
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const submitButton = document.querySelector(".submit-button");
  const resultDiv = document.querySelector(".result");

  submitButton.addEventListener("click", function () {
    submitButton.classList.add("fade-out");

    setTimeout(() => {
      submitButton.style.display = "none";
      if (resultDiv) {
        resultDiv.classList.add("show");
      }
    }, 500);
  });
});
