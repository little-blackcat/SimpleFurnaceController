var ctx = document.getElementById("chartCanvas").getContext("2d");

Chart.defaults.global.legend.display = false;

var chart;

if (typeof XMLHttpRequest == "undefined") {
    XMLHttpRequest = function() {
        //IE wykorzystuje biblioteki ActiveX do tworzenia obiektu XMLHttpRequest
        return new ActiveXObject(
            //IE5 używa innego obektu XMLHTTP niż IE6 i wyższe
            navigator.userAgent.indexOf("MSIE 5") >=0 ? "Microsoft.XMLHTTP" : "Msxml2.XMLHTTP"
        );
    }
}

function update_chart(hourLabel, temps){
    //console.log(hourLabel)
    //console.log(temps)

    var ourData = {
    	labels: hourLabel,
    	datasets: [
    		{
    			data: temps,
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
function ajax_get_temps(){
    var xml = new XMLHttpRequest();

    xml.open("GET", "_ajax_chart_hours_", true);

    xml.onreadystatechange = function(){
        if ( xml.readyState == 4 )
        {
            var newData = JSON.parse(xml.responseText);
            if(newData.isTempsInDatabase)
            {
                var hourLabel = newData.hourLabel;
                var temps = newData.temps;

                update_chart(hourLabel, temps)
            }
            else
            {
               //console.log("in database doesn't exist any temp logs from last 12 hours")
            }

            xml = null;
        }
    };

    xml.send();
}

setInterval(ajax_get_temps(), 120000);





	


