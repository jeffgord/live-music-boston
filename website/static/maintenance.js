$(document).ready(function () {
    fillLocationsTable();
    initializeSortableTable("locations", updateLocationsOrder);
});

var defaultOptions = {
    ordering: false,
    paging: false,
    searching: false,
    info: false
}

function fillLocationsTable() {
    $('#locations').DataTable($.extend({}, defaultOptions, {
        ajax: "/maintenance/locations",
        columns: [
            { data: "id" },
            { data: "name" },
            {
                data: null,
                defaultContent: '<i class="hoverable bi bi-pencil"/>',
                width: "6%"
            },
            {
                data: null,
                defaultContent: '<i class="hoverable bi bi-trash"/>',
                width: "6%"
            }
        ],
        drawCallback: function () {
            var hoverableElements = document.querySelectorAll('.hoverable');
            hoverableElements.forEach(changeFillOnHover);
        }
    }));
}

function updateLocationsOrder() {
    var order = $('#locations tbody').sortable('toArray', { attribute: 'data-location-id' });

    $.ajax({
        type: 'POST',
        url: '/maintenance/update-locations-order',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ id_order: order }),
        success: function () {
            location.reload();
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}