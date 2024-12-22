// document.addEventListener('DOMContentLoaded', function () {
//     const apiKey = '3e97304bbf1fa84a3c06c5ac61abb55c'; // Replace with your OpenWeatherMap API key
//     const city = 'Bangalore'; // Replace with your desired city
//     const weatherContainer = document.getElementById('weather-info');

//     async function fetchWeather() {
//         try {
//             const response = await fetch(
//                 `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`
//             );
//             const data = await response.json();
            
//             if (response.ok) {
//                 const { temp } = data.main;
//                 const { description } = data.weather[0];
//                 const weatherInfo = `The temperature in ${city} is ${temp}°C with ${description}.`;
//                 weatherContainer.textContent = weatherInfo;
//             } else {
//                 weatherContainer.textContent = `Error: ${data.message}`;
//             }
//         } catch (error) {
//             weatherContainer.textContent = 'Error fetching weather data.';
//         }
//     }

//     fetchWeather();
// });
// document.addEventListener('DOMContentLoaded', function () {
//     // Initialize Google Maps
//     function initMap() {
//         const location = { lat: 12.9716, lng: 77.5946 }; // Replace with your location coordinates
//         const map = new google.maps.Map(document.getElementById('map'), {
//             center: location,
//             zoom: 14,
//         });

//         // Add a marker
//         new google.maps.Marker({
//             position: location,
//             map: map,
//             title: 'Nearest Bus Station',
//         });
//     }

//     // Load the Google Maps script dynamically
//     const script = document.createElement('script');
//     script.src = 'https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap';
//     script.async = true;
//     script.defer = true;
//     document.head.appendChild(script);
// });
document.addEventListener('DOMContentLoaded', function () {
    const apiKey = '3e97304bbf1fa84a3c06c5ac61abb55c'; // Replace with your OpenWeatherMap API key
    const city = 'Bangalore'; // Replace with your desired city
    const weatherContainer = document.getElementById('weather-info');

    async function fetchWeather() {
        try {
            const response = await fetch(
                `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`
            );
            const data = await response.json();
            
            if (response.ok) {
                const { temp } = data.main;
                const { description } = data.weather[0];
                const weatherInfo = `The temperature in ${city} is ${temp}°C with ${description}.`;
                weatherContainer.textContent = weatherInfo;
            } else {
                weatherContainer.textContent = `Error: ${data.message}`;
            }
        } catch (error) {
            weatherContainer.textContent = 'Error fetching weather data.';
        }
    }

    fetchWeather();
});