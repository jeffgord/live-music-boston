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
                defaultContent: '<i class="hoverable bi hover-bi-pencil"/>',
            },
            {
                data: null,
                defaultContent: '<i class="hoverable bi hover-bi-trash"/>',
            }
        ]
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