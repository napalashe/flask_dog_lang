// script.js

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const selectionBoxes = document.querySelectorAll(".selection-box");
  const resultDiv = document.querySelector(".result");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting immediately

    // Fade out the selection boxes
    selectionBoxes.forEach((box) => {
      box.classList.add("fade-out");
    });

    // After the fade out completes, submit the form
    setTimeout(function () {
      form.submit(); // Now submit the form after the fade out
    }, 500); // Match the CSS transition duration for fade-out
  });

  // If there is a result to show, fade it in slowly
  if (resultDiv) {
    setTimeout(function () {
      resultDiv.classList.add("fade-in");
    }, 500); // Start fading in after a brief delay

    resultDiv.style.transition = "opacity 5s ease"; // Extend the fade-in duration to 5 seconds
  }
});
// script.js

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
    }, 500); // Wait for the fade-out animation to complete
  });
});
