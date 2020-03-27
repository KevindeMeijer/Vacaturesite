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
        result = result.split(",");
        result1 = result[0];
        result2 = result[2];
        result3 = result[4];
        result4 = result[6];
        result5 = result[8];
        Word2VecRes1.innerHTML = result1;
        Word2VecRes2.innerHTML = result2;
        Word2VecRes3.innerHTML = result3;
        Word2VecRes4.innerHTML = result4;
        Word2VecRes5.innerHTML = result5;
    });
}
