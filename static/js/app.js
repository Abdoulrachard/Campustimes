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
$.ajax({
  url: "get_capacity_data",
  type: "GET",
  success: function(response) {
    var capacityData = response.capacity_values;
    var levelCategories = response.level_categories;

    var barChartOptions = {
      series: [{
        data: capacityData,
        name: "Etudiants",
      }],
      chart: {
        type: "bar",
        background: "transparent",
        height: 450,
        toolbar: {
          show: false,
        },
      },
      colors: [
        "#2962ff",
        "#d50000",
        "#2e7d32",
        "#ff6d00",
        "#583cb3",
      ],
      plotOptions: {
        bar: {
          distributed: true,
          borderRadius: 4,
          horizontal: false,
          columnWidth: "50%",
        }
      },
      dataLabels: {
        enabled: false,
      },
      fill: {
        opacity: 1,
      },
      grid: {
        borderColor: "#55596e",
        yaxis: {
          lines: {
            show: true,
          },
        },
        xaxis: {
          lines: {
            show: true,
          },
        },
      },
      legend: {
        labels: {
          colors: "#f5f7ff",
        },
        show: true,
        position: "top",
      },
      stroke: {
        colors: ["transparent"],
        show: true,
        width: 2
      },
      tooltip: {
        shared: true,
        intersect: false,
        theme: "dark",
      },
      xaxis: {
        categories: levelCategories,
        title: {
          style: {
            color: "#f5f7ff",
          },
        },
        axisBorder: {
          show: true,
          color: "#55596e",
        },
        axisTicks: {
          show: true,
          color: "#55596e",
        },
        labels: {
          style: {
            colors: "#f5f7ff",
          },
        },
      },
      yaxis: {
        title: {
          text: "Statistiques des etudiants",
          style: {
            color:  "#f5f7ff",
          },
        },
        axisBorder: {
          color: "#55596e",
          show: true,
        },
        axisTicks: {
          color: "#55596e",
          show: true,
        },
        labels: {
          style: {
            colors: "#f5f7ff",
          },
        },
      }
    };

    var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
    barChart.render();
  },
  error: function(error) {
    console.log("Une erreur s'est produite lors de la récupération des données.");
  }
});
 

  document.addEventListener("DOMContentLoaded", function() {
    const dropdownMenu = document.getElementById("dropdownMenu");
    const image = document.querySelector(".nav-item.dropdown img");

    image.addEventListener("click", function(event) {
      event.preventDefault();
      dropdownMenu.classList.toggle("show");
    });
  });


