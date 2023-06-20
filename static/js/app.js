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

function updateFiliereOptions() {
  var semestreSelect = document.getElementById("semestre");
  var filiereGroup = document.getElementById("filiereGroup");
  var filiereSelect = document.getElementById("filiere");

  // Réinitialiser les options de la filière
  filiereSelect.innerHTML = "<option value='all'>Toutes les filières</option>";

  // Récupérer la valeur du semestre sélectionné
  var selectedSemestre = semestreSelect.value;

  // Afficher ou masquer les éléments en fonction du semestre sélectionné
  if (selectedSemestre === "semestre1" || selectedSemestre === "semestre2") {
    filiereGroup.style.display = "none";
  } else {
    filiereGroup.style.display = "block";

    // Ajouter les options de filière en fonction du semestre sélectionné
    var filieres = [
      "Génie Logiciel",
      "Sécurité Informatique",
      "Internet Multimédia",
      "Intelligence Artificielle",
      "Systèmes Embarqués et IoT"
    ];

    filieres.forEach(function (filiere) {
      var option = document.createElement("option");
      option.value = filiere.toLowerCase().replace(/\s/g, "-");
      option.textContent = filiere;
      filiereSelect.appendChild(option);
    });
  }
}

