const IconElements = {
    Add: "bi-plus-square",
    Edit: "bi-pencil",
    Delete: "bi-trash",
    Home: "icon-guitar"
}

function changeFillOnHover(element) {
    var iconClass;
    Object.keys(IconElements).forEach(function (key) {
        if (element.classList.contains(IconElements[key]))
            iconClass = IconElements[key];
    });

    var filledIconClass = iconClass + '-fill';

    function removeIconClasses() {
        if (element.classList.contains(iconClass)) element.classList.remove(iconClass);
        if (element.classList.contains(filledIconClass)) element.classList.remove(filledIconClass);
    }

    element.addEventListener('mouseover', function () {
        removeIconClasses();
        element.classList.add(filledIconClass);
    });
    element.addEventListener('mouseout', function () {
        removeIconClasses();
        element.classList.add(iconClass);
    })
}

document.addEventListener('DOMContentLoaded', function () {
    var hoverableElements = document.querySelectorAll('.hoverable');
    hoverableElements.forEach(changeFillOnHover);
});