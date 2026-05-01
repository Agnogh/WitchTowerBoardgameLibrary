// Find the "Cart link"
const cartLink = document.getElementById("cart-link");
// Find "toast box"
const cartToast = document.getElementById("cart-toast");
// find any form with 'class="js-feature-toast-form"'
const featureToastForms = document.querySelectorAll(".js-feature-toast-form");
// if both conditions are met (both elements are present)
let toastTimer;

  function showToast(message) {
    if (!cartToast) return;
    
    cartToast.textContent = message;
    cartToast.classList.add("is-visible");

    clearTimeout(toastTimer);

    toastTimer = setTimeout(function () {
      cartToast.classList.remove("is-visible");
    }, 3000);
  }

  // cart link
if (cartLink) {
  cartLink.addEventListener("click", function (event) {
    // prevvent user to go anywhere
    event.preventDefault();

    const message =
      cartLink.dataset.toastMessage ||
      "Cart system will be available in v1.2.";

    showToast(message);
  });
}

// Any future placeholder form submit
featureToastForms.forEach(function (form) {
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const message =
      form.dataset.toastMessage ||
      "This feature will be available in v1.2.";

    showToast(message);
  });
});
