function ingevoerd() {
    let invoer = document.getElementById('iets').value;



    fetch('http://127.0.0.1:8080/ingevoerd', {
        method: 'POST',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json' },
    }).then((data) => {
        return invoer.in
    })
}

var nummer = 9

