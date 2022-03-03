function get_weather(city){
    fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=ad01d6189690a68a663cd9aec2438a2d
    `)
    .then(response => response.json() )
    .then(geocode => {
        var lon = geocode[0].lon;
        var lat = geocode[0].lat;
        fetch(`http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=ad01d6189690a68a663cd9aec2438a2d`)
        .then(response => response.json() )
        .then(current => {
            console.log(current);
            var city_name = current.name;
            var current_desc = current.weather[0].description;
            var current_high = Math.round(current.main.temp_max);
            var current_low = Math.round(current.main.temp_min);
            var weather_id = current.weather[0].id;
            var icon = "#icon0";
            var date0 = new Date();

            document.querySelector('#city_name').innerHTML = city_name;
            document.querySelector('#current_desc').innerHTML = current_desc;
            document.querySelector('#high0').innerHTML = current_high;
            document.querySelector('#low0').innerHTML = current_low;
            document.querySelector('#date0').innerHTML = date0.toDateString();

            change_icon(icon, weather_id);

            })
        .catch(err => console.log(err));

        fetch(`http://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&units=metric&exclude=minutely,hourly&appid=ad01d6189690a68a663cd9aec2438a2d`)
        .then(response => response.json() )
        .then(forecast => {
            console.log(forecast);
            for (let i = 0; i < 3; i++) {
                var forecast_desc = forecast.daily[i].weather[0].description
                var weather_id = forecast.daily[i].weather[0].id
                var forecast_high = Math.round(forecast.daily[i].temp.max)
                var forecast_low = Math.round(forecast.daily[i].temp.min)
                var icon = '#icon' + (i+1)
                var date = new Date()
                date.setDate(date.getDate() + (i + 1))

                
                document.querySelector('#desc' + (i+1)).innerHTML = forecast_desc
                document.querySelector('#high' + (i+1)).innerHTML = forecast_high
                document.querySelector('#low' + (i+1)).innerHTML = forecast_low
                document.querySelector('#date' + (i+1)).innerHTML = date.toDateString();

                change_icon(icon, weather_id)
            }

            })
        })

        .catch(err => console.log(err))
    .catch(err => console.log(err) )
};

function change_icon(icon, weather_id){
    if (weather_id >= 200 && weather_id <= 599){
        document.querySelector(icon).src = "assets/some_rain.png"
    }   else if (weather_id > 800 && weather_id < 805){
        document.querySelector(icon).src = "assets/some_clouds.png"
    }   else if (weather_id = 800){
        document.querySelector(icon).src = "assets/some_sun.png"
    }   
}

function closeAlert(element) {
    var alertID = document.querySelector(element);
    alertID.style.display = 'none';
};

function temperature (choice) {
    var formula = choice.value;
    if (formula == "fahrenheit") {
        for (let i = 0; i < 4; i++) {
            var newHigh = document.querySelector('#high' + i).innerHTML;
            newHigh = Math.round(newHigh*1.8 + 32);
            document.querySelector('#high' + i).innerHTML = newHigh;
            var newLow = document.querySelector('#low' + i).innerHTML;
            newLow = Math.round(newLow*1.8 + 32);
            document.querySelector('#low' + i).innerHTML = newLow;
        }

    } else if (formula == "celcius") {
        for (let i = 0; i < 4; i++) {
            var highArr = [24,27,21,26];
            var lowArr = [18,19,16,21];
            document.querySelector('#high' + i).innerHTML = highArr[i];
            document.querySelector('#low' + i).innerHTML = lowArr[i];
        }
    }
};
