var el = document.getElementById("wrapper");
var toggleButton = document.getElementById("menu-toggle");
var navbar = document.querySelector(".navbar");

toggleButton.onclick = function () {
    el.classList.toggle("toggled");
    navbar.classList.toggle("collapsed");
};
