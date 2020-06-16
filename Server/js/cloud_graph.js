google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_cloud_security()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        [{v: 1, f: 'January'}, resultarray_cloud_security[0]],
        [{v: 2, f: 'February'}, resultarray_cloud_security[1]],
        [{v: 3, f: 'March'}, resultarray_cloud_security[2]],
        [{v: 4, f: 'April'}, resultarray_cloud_security[3]],
        [{v: 5, f: 'May'}, resultarray_cloud_security[4]],
        [{v: 6, f: 'Juno'}, resultarray_cloud_security[5]],
        [{v: 7, f: 'July'}, resultarray_cloud_security[6]],
        [{v: 8, f: 'August'}, resultarray_cloud_security[7]],
        [{v: 9, f: 'September'}, resultarray_cloud_security[8]],
        [{v: 10, f: 'Oktober'}, resultarray_cloud_security[9]],
        [{v: 11, f: 'November'}, resultarray_cloud_security[10]],
        [{v: 12, f: 'December'}, resultarray_cloud_security[11]]
    ]);

    var options = {
        title: 'Cloud & Security 2016',
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

    var chart = new google.visualization.LineChart(document.getElementById('cloudChart'));

    chart.draw(data, options);
}