document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // DELETE CONFIRMATION
    // ==========================

    document.querySelectorAll(".btn-delete").forEach(btn => {

        btn.addEventListener("click", function (e) {

            e.preventDefault();

            const url = this.href;

            Swal.fire({

                title: "Delete Area?",

                text: "This action cannot be undone.",

                icon: "warning",

                showCancelButton: true,

                confirmButtonColor: "#d33",

                confirmButtonText: "Delete",

                cancelButtonText: "Cancel"

            }).then((result) => {

                if (result.isConfirmed) {

                    window.location = url;

                }

            });

        });

    });


    // ==========================
    // NEW AREA
    // ==========================

    const addButton = document.querySelector('[data-bs-target="#addAreaModal"]');

    if (addButton) {

        addButton.addEventListener("click", function () {

            document.getElementById("modalTitle").innerText =
                "New Cleaning Area";

            document.getElementById("saveButton").innerText =
                "Save Area";

            document.getElementById("areaForm").action =
                "/areas/add";

            document.getElementById("areaForm").reset();

            document.getElementById("color").value =
                "#0d6efd";

            document.getElementById("active").checked = true;

        });

    }


    // ==========================
    // EDIT AREA
    // ==========================

    document.querySelectorAll(".btn-edit").forEach(btn => {

        btn.addEventListener("click", function () {

            document.getElementById("modalTitle").innerText =
                "Edit Cleaning Area";

            document.getElementById("saveButton").innerText =
                "Update Area";

            document.getElementById("areaForm").action =
                "/areas/edit/" + this.dataset.id;

            document.getElementById("area_code").value =
                this.dataset.code;

            document.getElementById("area_name").value =
                this.dataset.name;

            document.getElementById("category").value =
                this.dataset.category;

            document.getElementById("estimated_minutes").value =
                this.dataset.minutes;

            document.getElementById("display_order").value =
                this.dataset.order;

            document.getElementById("color").value =
                this.dataset.color;

            document.getElementById("remarks").value =
                this.dataset.remarks;

            document.getElementById("active").checked =
                (this.dataset.active === "True");

        });

    });

});