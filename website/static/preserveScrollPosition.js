function saveScrollPosition() {
    var scrollPosition = window.scrollY || document.documentElement.scrollTop;

    fetch("/maintenance/save-scroll-position", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: "scroll_position=" + encodeURIComponent(scrollPosition),
    }).catch(error => console.error("Error:", error));
}

document.addEventListener('DOMContentLoaded', function () {
    var postbackTriggers = document.querySelectorAll('.postback-trigger');

    postbackTriggers.forEach(function (element) {
        element.addEventListener('click', saveScrollPosition);
    });
});