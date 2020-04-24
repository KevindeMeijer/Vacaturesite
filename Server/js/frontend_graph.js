google.charts.load('current', {
    'packages': ['corechart']
});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'Low', 'High'],
        ['2005', 11, 13],
        ['2006', 13, 17],
        ['2007', 22, 25],
        ['2008', 21, 24],
        ['2009', 22, 33],
        ['2010', 20, 35],
        ['2011', 24, 34],
        ['2012', 26, 35],
        ['2013', 28, 37],
        ['2014', 35, 41],
        ['2015', 45, 56],
        ['2016', 61, 77],
        ['2017', 72, 85],
        ['2018', 81, 100],
        ['2019', 84, 100]
    ]);

    var options = {
        title: 'Front-End',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('frontEndChart'));

    chart.draw(data, options);
}