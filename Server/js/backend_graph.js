google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_backend()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        ['January', resultarray_backend[0]],
        ['February', resultarray_backend[1]],
        ['March', resultarray_backend[2]],
        ['April', resultarray_backend[3]],
        ['May', resultarray_backend[4]],
        ['Juno', resultarray_backend[5]],
        ['July', resultarray_backend[6]],
        ['August', resultarray_backend[7]],
        ['September', resultarray_backend[8]],
        ['Oktober', resultarray_backend[9]],
        ['November', resultarray_backend[10]],
        ['December', resultarray_backend[11]]
    ]);

    var options = {
        title: 'Back-End 2016',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('backEndChart'));

    chart.draw(data, options);
}