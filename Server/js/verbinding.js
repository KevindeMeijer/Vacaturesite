function ingevoerd() {
  let Word2VecRes1 = document.getElementById('Word2VecRes1');
  let Word2VecRes2 = document.getElementById('Word2VecRes2');
  let Word2VecRes3 = document.getElementById('Word2VecRes3');
  let Word2VecRes4 = document.getElementById('Word2VecRes4');
  let Word2VecRes5 = document.getElementById('Word2VecRes5');

  fetch('http://127.0.0.1:5000/ingevoerd', {
    method: 'GET',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
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

  let jsondata = { 'naam': naam, 'telefoonnummer': telefoonnummer, 'email_adres': email_adres, 'onderwerp': onderwerp, 'bericht': bericht };
  fetch('http://127.0.0.1:5000/report', {
    method: 'POST',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify(jsondata)
  }).then((response) => response.json());
  return false;
}

function load_reports() {
  fetch('http://127.0.0.1:5000/load_reports')
    .then(response => response.json())
    .then(result => {
      let table_1 = document.getElementById('admintable')
      for (var i = 0; i < result.length; ++i) {
        item = result[i]
        let new_row = table_1.insertRow(-1);
        
        let new_naam = new_row.insertCell(0);
        let new_text_naam = document.createTextNode(item.naam);
        new_naam.appendChild(new_text_naam);

        let new_telefoonnummer = new_row.insertCell(1);
        let new_text_telefoonnummer = document.createTextNode(item.telefoonnummer);
        new_telefoonnummer.appendChild(new_text_telefoonnummer);
        
        let new_email = new_row.insertCell(2);
        let new_text_email = document.createTextNode(item.email_adres);
        new_email.appendChild(new_text_email);

        let new_onderwerp = new_row.insertCell(3);
        let new_text_onderwerp = document.createTextNode(item.onderwerp);
        new_onderwerp.appendChild(new_text_onderwerp)

        let new_bericht = new_row.insertCell(4);
        let new_text_bericht = document.createTextNode(item.bericht);
        new_bericht.appendChild(new_text_bericht)
      }


    })
    .catch(console.error);
}

// Grafieken maken
resultarray_frontend = []
function load_chars_frontend() {
    fetch('http://127.0.0.1:5000/load_chars_frontend')
    .then(response => response.json())
    .then(result =>{
        resultarray_frontend = result
    })
}
resultarray_backend = []
function load_chars_backend() {
    fetch('http://127.0.0.1:5000/load_chars_backend')
    .then(response => response.json())
    .then(result =>{
        resultarray_backend = result
    })
}
resultarray_productowner = []
function load_chars_productowner() {
    fetch('http://127.0.0.1:5000/load_chars_productowner')
    .then(response => response.json())
    .then(result =>{
        resultarray_productowner = result
    })
}
resultarray_cloud_security = []
function load_chars_cloud_security() {
    fetch('http://127.0.0.1:5000/load_chars_cloud_security')
    .then(response => response.json())
    .then(result =>{
        resultarray_cloud_security = result
    })
}