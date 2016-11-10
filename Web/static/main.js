var chartIsCreated = false

var ctx = document.getElementById('chartCanvas').getContext("2d");

Chart.defaults.global.legend.display = false;

var chart;

if (typeof XMLHttpRequest == "undefined")
{
    XMLHttpRequest = function() {
        //IE wykorzystuje biblioteki ActiveX do tworzenia obiektu XMLHttpRequest
        return new ActiveXObject(
            //IE5 używa innego obektu XMLHTTP niż IE6 i wyższe
            navigator.userAgent.indexOf("MSIE 5") >=0 ? "Microsoft.XMLHTTP" : "Msxml2.XMLHTTP"
        );
    }
}
function create_chart(labels, dataset){
    var ourData = {
    	labels: labels,
    	datasets: [
    		{
    			data: dataset,
    			borderColor: "blue",
    			fill: false

    		}
    	]
    }
    chart = new Chart.Line(ctx, {
    	data: ourData,
    	option: {
    	    legend: {
    	        display: false
            },
    		responsive: true,
    		maintainAspectRatio: true,
    		animation: false,

    	}
    });
}
function update_chart(labels, temps, pointNum){
    var lastLabel = labels[labels.length - 1];
    var lastTemps = temps[temps.length - 1];

    var chartData = chart.data.datasets[0].data

    var chartLabels = chart.data.labels

    var lastIndex = chartData.length - 1;

    if(lastLabel != chartLabels[lastIndex])
    {

        chartData.push(lastTemps);
        chartLabels.push(lastLabel);

        if(lastIndex >= (pointNum - 1))
        {
            chartData.shift();
            chartLabels.shift();
        }

        chart.update();
    }
    else
    {
        chartData[lastIndex] = lastTemps;
        chartLabels[lastIndex] = lastLabel;

        chart.update();
    }
}