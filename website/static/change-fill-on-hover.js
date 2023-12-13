document.addEventListener('DOMContentLoaded', function () {
    var hoverableElements = document.querySelectorAll('.hoverable');

    hoverableElements.forEach(function (element) {
        var iconClass = Array.from(element.classList).find(item => item.startsWith("hover-"));
        if (iconClass) {
            var iconClassWithoutPrefix = iconClass.replace("hover-", "");
            element.classList.add(iconClassWithoutPrefix);

            var iconClassWithFill = iconClassWithoutPrefix + "-fill";

            element.addEventListener('mouseover', function () {
                element.classList.remove(iconClassWithoutPrefix);
                element.classList.add(iconClassWithFill);
            });

            element.addEventListener('mouseout', function () {
                element.classList.remove(iconClassWithFill);
                element.classList.add(iconClassWithoutPrefix);
            });
        }
    });
});
