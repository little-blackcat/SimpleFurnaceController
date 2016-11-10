function ajax_get_temps(){
    var xml = new XMLHttpRequest();

    xml.open("GET", "/_ajax_chart_last_hour_", true);

    xml.onreadystatechange = function(){
        if ( xml.readyState == 4 )
        {
            console.log("interval function");
            var newData = JSON.parse(xml.responseText);
            if(newData.isTempsInDatabase)
            {
                var minuteLabel = newData.minuteLabel;
                var temps = newData.temps;
                console.log(minuteLabel);
                console.log(temps);
                if(chartIsCreated) update_chart(minuteLabel, temps, 60);
                else {
                    create_chart(minuteLabel, temps);
                    chartIsCreated = true;
                }
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

setInterval(ajax_get_temps, 2000);