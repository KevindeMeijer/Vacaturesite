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
};