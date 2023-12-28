/* document.getElementById("formCheckout").addEventListener("submit", function (e) {
    e.preventDefault();

    let form = e.target;

    // Utiliser SweetAlert pour demander une confirmation
    Swal.fire({
        title: 'Confirmation',
        text: "Etes-vous sûr de vouloir valider la commande?",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmer',
        cancelButtonText: 'Annuler'
    }).then((result) => {
        if (result.isConfirmed) {
            // Récupérer les valeurs du formulaire
            let first_name = form.first_name.value;
            let last_name = form.last_name.value;
            let email = form.email.value;
            let phone = form.phone_number.value;
            let country = form.country.value;
            let city = form.city.value;
            let street = form.street.value;
            let door = form.door.value;
            let compagnie = form.compagnie.value;
            let payement = document.querySelector('input[name="payment"]:checked').value;

            let shippingformData = {
                first_name: first_name,
                last_name: last_name,
                email: email,
                phone: phone,
                country: country,
                city: city,
                street: street,
                door: door,
                compagnie: compagnie,
                payement: payement,
                total: total,
            };
            console.log("FormData:", shippingformData)

            myUrl = window.location.origin;
            url = myUrl + "/boutique/payement/";

            fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
                body: JSON.stringify({ shippingformData: shippingformData }),
            })
            .then((response) => response.json())
            .then((data) => {
                console.log("Success:", data);
                // Afficher un message de succès avec SweetAlert
                Swal.fire({
                    title: 'Commande Validée!',
                    text: 'Votre commande a été enregistrée avec succès.',
                    icon: 'success'
                }).then(() => {
                    // Rediriger l'utilisateur vers la page d'accueil
                    home = window.location.origin;
                    window.location.href = home;
                });
            });
        }
    });
});
 */
document.getElementById("formCheckout").addEventListener("submit", function (e) {
    e.preventDefault();

    let form = e.target;

    // Utiliser SweetAlert pour demander une confirmation
    Swal.fire({
        title: 'Confirmation',
        text: "Etes-vous sûr de vouloir valider la commande?",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmer',
        cancelButtonText: 'Annuler'
    }).then((result) => {
        if (result.isConfirmed) {
            // L'utilisateur a confirmé, afficher un message de chargement
            Swal.fire({
                title: 'Chargement en cours...',
                text: 'Veuillez patienter pendant que nous traitons votre commande.',
                icon: 'info',
                showCancelButton: false,
                showConfirmButton: false,
                allowOutsideClick: false,
            });

            // Récupérer les valeurs du formulaire
            let first_name = form.first_name.value;
            let last_name = form.last_name.value;
            let email = form.email.value;
            let phone = form.phone_number.value;
            let country = form.country.value;
            let city = form.city.value;
            let street = form.street.value;
            let door = form.door.value;
            let compagnie = form.compagnie.value;
            let payement = document.querySelector('input[name="payment"]:checked').value;

            let shippingformData = {
                first_name: first_name,
                last_name: last_name,
                email: email,
                phone: phone,
                country: country,
                city: city,
                street: street,
                door: door,
                compagnie: compagnie,
                payement: payement,
                total: total,
            };
            console.log("FormData:", shippingformData)

            myUrl = window.location.origin;
            url = myUrl + "/boutique/payement/";

            fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
                body: JSON.stringify({ shippingformData: shippingformData }),
            })
            .then((response) => response.json())
            .then((data) => {
                console.log("Success:", data);
                // Masquer le message de chargement
                Swal.close();

                // Afficher un message de succès avec SweetAlert
                Swal.fire({
                    title: 'Commande Validée!',
                    text: 'Votre commande a été enregistrée avec succès.',
                    icon: 'success'
                }).then(() => {
                    // Rediriger l'utilisateur vers la page d'accueil
                    home = window.location.origin;
                    window.location.href = home;
                });
            })
            .catch((error) => {
                // Masquer le message de chargement en cas d'erreur
                Swal.close();

                // Afficher une alerte SweetAlert avec l'erreur
                Swal.fire({
                    title: 'Erreur',
                    text: 'Une erreur est survenue lors du traitement de votre commande: ' + error.message,
                    icon: 'error',
                });
            });
        }
    });
});
