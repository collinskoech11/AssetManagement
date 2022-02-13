var stars = [230000,200000,160000,220000,180000,190000,210000,150000,160000,200000,150000,160000]
var frameworks = ['January','February','March','April','May','June','July','August','September','November','December']
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: frameworks,
        datasets : [{
            label: 'Monthly Payment total',
            data: stars,
            backgroundColor: "#01030D",
            borderColor: "#fff"

        }]
    },
    options:{
        maintainAspectRatio: false,
        responsive: false
    },
    scales: {
        y: {
            max: 5,
            min: 0,
            ticks: {
                stepSize: 0.5
            }
        }
    }
 }
)