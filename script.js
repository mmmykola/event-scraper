
document.addEventListener('DOMContentLoaded', function() {
    fetch('/events')
        .then(response => response.json())
        .then(events => {
            const container = document.getElementById('events-container');
            events.forEach(event => {
                let div = document.createElement('div');
                div.innerHTML = `<h2>${event.title}</h2><p>${event.date}</p><a href="${event.link}" target="_blank">Event Link</a>`;
                container.appendChild(div);
            });
        });
});
