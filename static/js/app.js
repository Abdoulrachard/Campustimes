$(document).ready(function () {
  "use strict";

  let el = document.getElementById("wrapper");
  let navbar = document.querySelector(".navbar");

  $("#menu-toggle").on("click", function () {
    el.classList.toggle("toggled");
    navbar.classList.toggle("collapsed");
  });

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
          $("#loading").hide();
        },
        error: function (err) {
          console.error(err);
        },
        beforeSend: function () {
          $("#loading").show();
        },
      });

      $(".ajaxForm").each(function (k, elt) {
        $(this).on("submit", function (e) {
          e.preventDefault();

          const formData = $(this).serialize();

          $.ajax({
            method: $(this).attr("method"),
            url: $(this).attr("action"),
            data: formData,
            success: function (data) {
              $("#mainPage").html(data);
            },
            error: function (err) {
              console.error(err);
            },
          });
        });
      });
    });
  });
});
