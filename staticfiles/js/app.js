let ajoutBtn = document.getElementsByClassName('ajout-panier');

for(i = 0; i < ajoutBtn.length; i++){
    ajoutBtn[i].addEventListener('click', function(){

        let productID =this.dataset.product
        let action = this.dataset.action

        console.log('Produit id: ', productID, 'Action: ', action)
        console.log('USER: ', user)

        updateUserOrder(productID, action) 
    })
}

function updateUserOrder(productID, action){
    console.log('Utilisateur authentifier, envoie des donnees ...')

    // Adapter l'url a celle de la vue de django
    const myUrl = window.location.origin;
   
    let url = myUrl + "/ajout-au-panier/";
  
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application.json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })
    .then((Response) => {
        return Response.json();
    })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    });
}