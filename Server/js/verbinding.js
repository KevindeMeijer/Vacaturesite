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

function load_chars_frontend() {
    fetch('http://127.0.0.1:5000/load_chars_frontend')
    .then(response => response.json())
    .then(result =>{
        jan_f = result[0]
        feb_f = result[1]
        mrt_f = result[2]
        apr_f = result[3]
        mei_f = result[4]
        jun_f = result[5]
        jul_f = result[6]
        aug_f = result[7]
        sep_f = result[8]
        okt_f = result[9]
        nov_f = result[10]
        dec_f = result[11]
    })
}

function load_chars_backend() {
    fetch('http://127.0.0.1:5000/load_chars_backend')
    .then(response => response.json())
    .then(result =>{
        jan_b = result[0]
        feb_b = result[1]
        mrt_b = result[2]
        apr_b = result[3]
        mei_b = result[4]
        jun_b = result[5]
        jul_b = result[6]
        aug_b = result[7]
        sep_b = result[8]
        okt_b = result[9]
        nov_b = result[10]
        dec_b = result[11]
    })
}
function load_chars_productowner() {
    fetch('http://127.0.0.1:5000/load_chars_productowner')
    .then(response => response.json())
    .then(result =>{
        jan_p = result[0]
        feb_p = result[1]
        mrt_p = result[2]
        apr_p = result[3]
        mei_p = result[4]
        jun_p = result[5]
        jul_p = result[6]
        aug_p = result[7]
        sep_p = result[8]
        okt_p = result[9]
        nov_p = result[10]
        dec_p = result[11]
    })
}
function load_chars_cloud_security() {
    fetch('http://127.0.0.1:5000/load_chars_cloud_security')
    .then(response => response.json())
    .then(result =>{
        jan_c = result[0]
        feb_c = result[1]
        mrt_c = result[2]
        apr_c = result[3]
        mei_c = result[4]
        jun_c = result[5]
        jul_c = result[6]
        aug_c = result[7]
        sep_c = result[8]
        okt_c = result[9]
        nov_c = result[10]
        dec_c = result[11]
    })
}