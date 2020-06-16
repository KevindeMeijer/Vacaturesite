google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_productowner()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        ['January', resultarray_productowner[0]],
        ['February', resultarray_productowner[1]],
        ['March', resultarray_productowner[2]],
        ['April', resultarray_productowner[3]],
        ['May', resultarray_productowner[4]],
        ['Juno', resultarray_productowner[5]],
        ['July', resultarray_productowner[6]],
        ['August', resultarray_productowner[7]],
        ['September', resultarray_productowner[8]],
        ['Oktober', resultarray_productowner[9]],
        ['November', resultarray_productowner[10]],
        ['December', resultarray_productowner[11]]
    ]);

    var options = {
        title: 'Productowner 2016',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('poChart'));

    chart.draw(data, options);
}