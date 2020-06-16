google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_backend()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        [{v: 1, f: 'January'}, resultarray_backend[0]],
        [{v: 2, f: 'February'}, resultarray_backend[1]],
        [{v: 3, f: 'March'}, resultarray_backend[2]],
        [{v: 4, f: 'April'}, resultarray_backend[3]],
        [{v: 5, f: 'May'}, resultarray_backend[4]],
        [{v: 6, f: 'Juno'}, resultarray_backend[5]],
        [{v: 7, f: 'July'}, resultarray_backend[6]],
        [{v: 8, f: 'August'}, resultarray_backend[7]],
        [{v: 9, f: 'September'}, resultarray_backend[8]],
        [{v: 10, f: 'Oktober'}, resultarray_backend[9]],
        [{v: 11, f: 'November'}, resultarray_backend[10]],
        [{v: 12, f: 'December'}, resultarray_backend[11]]
    ]);

    var options = {
        title: 'Back-End 2016',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        },
        trendlines: {
            0: {type: 'linear', color: '#000', opacity: 0.5}
        },
        hAxis: {
            ticks: [{v: 1, f: 'January'}, {v: 2, f: 'February'}, {v: 3, f: 'March'}, {v: 4, f: 'April'}, {v: 5, f: 'May'}, {v: 6, f: 'Juno'}, {v: 7, f: 'July'}, {v: 8, f: 'August'}, {v: 9, f: 'September'}, {v: 10, f: 'Oktober'}, {v: 11, f: 'November'}, {v: 12, f: 'December'}]
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('backEndChart'));

    chart.draw(data, options);
}