function ingevoerd() {
    let vacature_id = document.getElementById('vacature_id');



    fetch('http://127.0.0.1:5000/ingevoerd', {
        method: 'GET',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json' },
    }).then((response) => {
        return response.json();
      })
      .then((result) => {
        vacature_id.innerHTML = result;
    });
}