// Find the "Cart link"
const cartLink = document.getElementById("cart-link");
// Find "toast box"
const cartToast = document.getElementById("cart-toast");
// if both conditions are met (both elements are present)
if (cartLink && cartToast) {
  let toastTimer;

  cartLink.addEventListener("click", function (event) {
    // prevvent user to go anywhere
    event.preventDefault();

    // show hidden msg
    cartToast.classList.add("is-visible");

  });
}