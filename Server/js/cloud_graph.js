google.charts.load('current', {
    'packages': ['corechart']
});
load_chars_cloud_security()

google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Trend'],
        ['January', resultarray_cloud_security[0]],
        ['February', resultarray_cloud_security[1]],
        ['March', resultarray_cloud_security[2]],
        ['April', resultarray_cloud_security[3]],
        ['May', resultarray_cloud_security[4]],
        ['Juno', resultarray_cloud_security[5]],
        ['July', resultarray_cloud_security[6]],
        ['August', resultarray_cloud_security[7]],
        ['September', resultarray_cloud_security[8]],
        ['Oktober', resultarray_cloud_security[9]],
        ['November', resultarray_cloud_security[10]],
        ['December', resultarray_cloud_security[11]]
    ]);

    var options = {
        title: 'Cloud & Security 2016',
        // curveType: 'function',
        legend: {
            position: 'bottom'
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('cloudChart'));

    chart.draw(data, options);
}