let main_menu = document.getElementById("main-dropdown-menu");
let learn_menu = document.getElementById("learn-dropdown-menu");
let services_menu = document.getElementById("services-dropdown-menu");
let blog_menu = document.getElementById("blog-dropdown-menu");
let contact_menu = document.getElementById("contact-dropdown-menu");

let menus = [
    main_menu,
    learn_menu,
    services_menu,
    blog_menu,
    contact_menu,
]

function open_main_menu() {
    main_menu.style.display = 'block';
}
function close_main_menu() {
    main_menu.style.display = 'none';
}
function open_learn_menu() {
    learn_menu.style.display = 'block';
}
function close_learn_menu() {
    learn_menu.style.display = 'none';
}
function open_services_menu() {
    services_menu.style.display = 'block';
}
function close_services_menu() {
    services_menu.style.display = 'none';
}
function open_blog_menu() {
    blog_menu.style.display = 'block';
}
function close_blog_menu() {
    blog_menu.style.display = 'none';
}
function open_contact_menu() {
    contact_menu.style.display = 'block';
}
function close_contact_menu() {
    contact_menu.style.display = 'none';
}
function close_all_menus() {
    var i;
    for (i = 0; i < menus.length; i++) {
        menus[i].style.display = 'none';
    }
}
function toggle_main_menu() {
    if (main_menu.style.display === "block") {
        close_main_menu()
    } else {
        close_all_menus();
        open_main_menu()
    }
}
function toggle_learn_menu() {
    if (learn_menu.style.display === "block") {
        close_learn_menu()
    } else {
        close_all_menus();
        open_learn_menu()
    }
}
function toggle_services_menu() {
    if (services_menu.style.display === "block") {
        close_services_menu()
    } else {
        close_all_menus()
        open_services_menu()
    }
}
function toggle_blog_menu() {
    if (blog_menu.style.display === "block") {
        close_blog_menu()
    } else {
        close_all_menus()
        open_blog_menu()
    }
}
function toggle_contact_menu() {
    if (contact_menu.style.display === "block") {
        close_contact_menu()
    } else {
        close_all_menus()
        open_contact_menu()
    }
}

function set_timezone() {
    const stz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
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
