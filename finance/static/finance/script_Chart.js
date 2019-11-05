// Chart Income
var ctx = document.getElementById('myChartIncome');
console.log(jsonDataI)
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: jsonDataI.labels,
        datasets: [{
            label: '',
            data: jsonDataI.default,
            backgroundColor: [
                'rgba(255, 99, 132)',
                'rgba(54, 162, 235)',
                'rgba(255, 206, 86)',
                'rgba(75, 192, 192)',
                'rgba(153, 102, 255)',
                'rgba(255, 159, 64)'
            ],
            borderWidth: 0
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Income'
        }
    }
});

// Chart Expense
var ctx = document.getElementById('myChartExpense');
console.log(jsonDataI)
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: jsonDataE.labels,
        datasets: [{
            label: '',
            data: jsonDataE.default,
            backgroundColor: [
                'rgba(255, 99, 132)',
                'rgba(54, 162, 235)',
                'rgba(255, 206, 86)',
                'rgba(75, 192, 192)',
                'rgba(153, 102, 255)',
                'rgba(255, 159, 64)'
            ],
            borderWidth: 0
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Expense'
        }
    }
});
