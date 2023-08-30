document.getElementById("formCheckout").addEventListener("submit", function (e) {
    e.preventDefault();
    
    let form = e.target;

    if (confirm("Etes-vous sûr de vouloir valider la commande?")) {
        // Récupérer les valeurs du formulaire
        let first_name = form.first_name.value;
        let last_name = form.last_name.value;
        let email = form.email.value;
        let phone = form.phone.value;
        let country = form.country.value;
        let city = form.city.value;
        let street = form.street.value;
        let door = form.door.value;
        let compagnie = form.compagnie.value;
        let payement = document.querySelector('input[name="payement"]:checked').value;

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
        document.getElementById("confirmButton").addEventListener("click", function () {
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
                // Fermer la modal
                $('#confirmationModal').modal('hide');
                // Afficher l'alerte de remerciement
                alert(`Merci pour votre commande!`);
                thanks = window.location.origin;
                window.location.href = thanks + "/boutique/thanks";
            });
        });
    }
});
