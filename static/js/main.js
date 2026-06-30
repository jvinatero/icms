document.addEventListener("DOMContentLoaded", () => {

    // ===========================
    // SweetAlert Delete Confirm
    // ===========================

    document.querySelectorAll(".btn-delete").forEach(button => {

        button.addEventListener("click", function (e) {

            e.preventDefault();

            const url = this.getAttribute("href");

            Swal.fire({
                title: "Delete Group?",
                text: "This action cannot be undone.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#dc3545",
                cancelButtonColor: "#6c757d",
                confirmButtonText: "Delete",
                cancelButtonText: "Cancel",
                reverseButtons: true
            }).then((result) => {

                if (result.isConfirmed) {
                    window.location.href = url;
                }

            });

        });

    });


    // ===========================
    // Auto Focus on Modal
    // ===========================

    const groupModal = document.getElementById("groupModal");

    if (groupModal) {

        groupModal.addEventListener("shown.bs.modal", () => {

            const input = groupModal.querySelector("input[name='group_name']");

            if (input) {
                input.focus();
                input.select();
            }

        });

    }


    // ===========================
    // Auto Hide Alerts
    // ===========================

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {

        setTimeout(() => {

            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();

        }, 3000);

    });

});