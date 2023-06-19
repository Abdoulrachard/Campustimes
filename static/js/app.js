(function () {
  "use strict";

  let el = document.getElementById("wrapper");
  let toggleButton = document.getElementById("menu-toggle");
  let navbar = document.querySelector(".navbar");

  toggleButton.onclick = function () {
    el.classList.toggle("toggled");
    navbar.classList.toggle("collapsed");
  };

  $(".c-link").each(function (k, elt) {
    $(this).on("click", function (ev) {
      ev.preventDefault();

      const url = $(this).data("c-link");

      const setBg = function (el) {
        $(".c-link").each(function (k, elt) {
          $(this).removeClass("c-link-active").addClass("bg-transparent");
        });
        $(el).addClass("c-link-active").removeClass("bg-transparent");
      };

      $.ajax({
        method: "GET",
        url: url,
        success: function (data) {
          $("#mainPage").html(data);
          setBg(elt);
          $('#loading').hide();
        },
        fail: function (err) {},
        beforeSend: function () {
            $('#loading').show();
        },
      });
    });
  });
})();

