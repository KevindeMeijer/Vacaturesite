function ingevoerd() {
    let vacature_id = document.getElementById('vacature_id').value;



    fetch('http://127.0.0.1:5000/ingevoerd', {
        method: 'GET',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json' },
    }).then((data) => {
        return vacature_id.innerHTML = goed
    })
}