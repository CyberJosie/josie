
function toggle_menu() {
    let menu = document.getElementById("dropdown-menu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

function set_timezone() {
    const stz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location = window.location.pathname;
        }
    };
    xhr.open("POST", "{% url 'set_timezone' %}", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', "{{csrf_token}}");
    
    xhr.send(
        JSON.stringify({
        "csrfmiddlewaretoken": "{{csrf_token}}",
        "timezone": stz,
    }));
}