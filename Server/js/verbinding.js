function ingevoerd() {
    let Word2VecRes1 = document.getElementById('Word2VecRes1');
    let Word2VecRes2 = document.getElementById('Word2VecRes2');
    let Word2VecRes3 = document.getElementById('Word2VecRes3');
    let Word2VecRes4 = document.getElementById('Word2VecRes4');
    let Word2VecRes5 = document.getElementById('Word2VecRes5');

    fetch('http://127.0.0.1:5000/ingevoerd', {
        method: 'GET',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json' },
    }).then((response) => {
        return response.json();
      })
      .then((result) => {
          result = result.split(") (");
          result1 = result[0];
          result2 = result[1];
          result3 = result[2];
          result4 = result[3];
          result5 = result[4];

          Word2VecRes1.innerHTML = result1;
          Word2VecRes2.innerHTML = result2;
          Word2VecRes3.innerHTML = result3;
          Word2VecRes4.innerHTML = result4;
          Word2VecRes5.innerHTML = result5;
    });
}
function report() {
    let naam = document.getElementById('fname').value;
    let telefoonnummer = document.getElementById('tel').value;
    let email_adres = document.getElementById('email').value;
    let onderwerp = document.getElementById('subject').value;
    let bericht = document.getElementById('message').value;

    let jsondata = { 'naam': naam, 'telefoonnummer': telefoonnummer, 'email_adres': email_adres, 'onderwerp': onderwerp, 'bericht': bericht};
    fetch('http://127.0.0.1:5000/report', {
        method: 'POST',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
        body: JSON.stringify(jsondata)
    }).then((response) => {
        return response.json();
    });
    return false;
}

window.onload   = () => console.log('window.onload works');

function load_reports() {
    let naam_1 = document.getElementById('naam_1');
    let telefoonnummer_1 = document.getElementById('telefoonnummer_1');
    let mail_1 = document.getElementById('mail_1');
    let onderwerp_1 = document.getElementById('onderwerp_1');
    let bericht_1 = document.getElementById('bericht_1');

window.onload = () => {
    fetch('http://127.0.0.1:5000/load_reports')
        .then(response => response.json())
        .then(result => {
            console.log(result)
            result = result.split(") (");
            result_id_contact = result[0];
            result_naam = result[1];
            result_telefoonnummer = result[2];
            result_mail = result[3];
            result_onderwerp = result[4];
            result_bericht = result[5];

            naam_1.innerHTML = result_naam;
            telefoonnummer_1.innerHTML = result_telefoonnummer;
            mail_1.innerHTML = result_mail;
            onderwerp_1.innerHTML = result_onderwerp;
            bericht_1.innerHTML = result_bericht;
    })
    .catch(console.error);
    }
}