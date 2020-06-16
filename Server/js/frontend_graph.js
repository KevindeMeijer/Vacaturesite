google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_frontend()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        ['January', resultarray_frontend[0]],
        ['February', resultarray_frontend[1]],
        ['March', resultarray_frontend[2]],
        ['April', resultarray_frontend[3]],
        ['May', resultarray_frontend[4]],
        ['Juno', resultarray_frontend[5]],
        ['July', resultarray_frontend[6]],
        ['August', resultarray_frontend[7]],
        ['September', resultarray_frontend[8]],
        ['Oktober', resultarray_frontend[9]],
        ['November', resultarray_frontend[10]],
        ['December', resultarray_frontend[11]]
    ]);

    var options = {
        title: 'Front-End 2016',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('frontEndChart'));

    chart.draw(data, options);
}
