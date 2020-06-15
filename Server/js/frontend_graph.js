google.charts.load('current', {
    'packages': ['corechart']
});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        ['January', 11],
        ['February', 17],
        ['March', 25],
        ['April', 24],
        ['May', 97],
        ['Juno', 1],
        ['July', 99],
        ['August', 14],
        ['September', 35],
        ['Oktober', 37],
        ['November', 41],
        ['December', 109]
    ]);

    var options = {
        title: 'Front-End 2016',
        curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('frontEndChart'));

    chart.draw(data, options);
}
