document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("menu-toggle");
  const menu = document.getElementById("menu-mobile");

  toggle.addEventListener("click", () => {
    menu.classList.toggle("active");
  });

  document.addEventListener("click", (e) => {
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      menu.classList.remove("active");
    }
  });
});
