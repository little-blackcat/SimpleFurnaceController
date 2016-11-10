function ajax_get_temps(){
    var xml = new XMLHttpRequest();

    xml.open("GET", "_ajax_chart_halfday_", true);

    xml.onreadystatechange = function(){
        if ( xml.readyState == 4 )
        {
            console.log("interval function");
            var newData = JSON.parse(xml.responseText);
            if(newData.isTempsInDatabase)
            {
                var hourLabel = newData.hourLabel;
                var temps = newData.temps;

                if(chartIsCreated) update_chart(hourLabel, temps, 12);
                else {
                    create_chart(hourLabel, temps);
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