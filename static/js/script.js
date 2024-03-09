function getWeather() {
    const locationInput = document.getElementById('locationInput').value;


    $.ajax({
        url: `/weather/?city=${encodeURIComponent(locationInput.split(',')[0])}&country=${encodeURIComponent(locationInput.split(',')[1])}`,
        method: 'GET',
        success: function (data) {
            if ('error' in data) {
                alert(data.error);
            } else {
                updateUI(data);
            }
        },
        error: function (error) {
            console.error('Error fetching weather data:', error);
            alert('Failed to fetch weather data. Please try again later.');
        }
    });
}

function updateUI(data) {
    const weatherInfo = document.getElementById('weather-info');

    weatherInfo.innerHTML = `
        <h2>${data.city}, ${data.country}</h2>
        <p>Temperature: ${data.temperature} °C</p>
        <p>Condition: ${data.condition}</p>
        <p>Humidity: ${data.humidity}%</p>
        <P>Wind Speed: ${data.wind_speed} meter/sec</P>
        
    `;
    weatherInfo.style.display = 'block';
}

