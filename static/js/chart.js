google.charts.load('current', { 'packages': ['line'] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Day');
    data.addColumn('number', 'Havo namligi');
    data.addColumn('number', 'Havo harorati');
    data.addColumn('number', 'Tuproq namligi');
    data.addRows([
        [1, 37, 20, 41],
        [2, 30, 18, 100],
        [3, 45, 23, 95],
        [4, 50, 25, 87],
        [5, 43, 21, 80],
        [6, 65, 27, 72],
        [7, 54, 29, 65],
        [8, 45, 32, 50],
        [9, 30, 26, 45],
        [10, 65, 28, 36],
        [11, 78, 23, 80],
        [12, 54, 26, 74],
        [13, 52, 21, 68],
        [14, 47, 29, 60]
    ]);
    var options = {
        chart: {
            title: 'DB Agro',
            subtitle: 'Sizning qurilmalaringiz'
        },
        width: 1200,
        height: 500,
        axes: {
            x: {
                0: { side: 'bottom' }
            }
        }
    };
    var chart = new google.charts.Line(document.getElementById('line_top_x'));
    chart.draw(data, google.charts.Line.convertOptions(options));
}