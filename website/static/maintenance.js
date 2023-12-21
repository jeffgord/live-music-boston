$(document).ready(function () {
    var btnAddLocation = document.getElementById('btn-add-location');
    var modalAddLocation = new bootstrap.Modal(document.getElementById('modal-add-location'));
    btnAddLocation.addEventListener('click', function () {
        modalAddLocation.show();
    });

    var modalEditLocation = new bootstrap.Modal(document.getElementById('modal-edit-location'));
    document.querySelectorAll('.modal-trigger-edit-location').forEach(function (button) {
        button.addEventListener('click', function () {
            var locationId = this.getAttribute('data-location-id');
            var oldName = this.getAttribute('data-location-name');
            document.getElementById('edit-location-id').value = locationId;
            document.getElementById('edit-location-name').value = oldName;
            modalEditLocation.show();
        });
    });

    var modalDeleteLocation = new bootstrap.Modal(document.getElementById('modal-delete-location'));
    document.querySelectorAll('.modal-trigger-delete-location').forEach(function (button) {
        button.addEventListener('click', function () {
            var locationId = this.getAttribute('data-location-id');
            document.getElementById('delete-location-id').value = locationId;
            document.getElementById('title-delete-location').textContent += this.getAttribute('data-location-name');
            modalDeleteLocation.show();
        });
    });

    var modalAddVenue = new bootstrap.Modal(document.getElementById('modal-add-venue'));
    document.querySelectorAll('.modal-trigger-add-venue').forEach(function (button) {
        button.addEventListener('click', function () {
            document.getElementById('add-select-venue-location').value = this.getAttribute('data-location-id');
            modalAddVenue.show();
        });
    });

    var modalEditVenue = new bootstrap.Modal(document.getElementById('modal-edit-venue'));
    document.querySelectorAll('.modal-trigger-edit-venue').forEach(function (button) {
        button.addEventListener('click', function () {
            document.getElementById('edit-venue-id').value = this.getAttribute('data-venue-id');
            document.getElementById('edit-venue-name').value = this.getAttribute('data-venue-name');
            document.getElementById('edit-venue-link').value = this.getAttribute('data-venue-link');;
            document.getElementById('edit-select-venue-location').value = this.getAttribute('data-venue-location-id');
            document.getElementById('edit-venue-frequency').value = this.getAttribute('data-venue-frequency');;
            document.getElementById('edit-venue-genre').value = this.getAttribute('data-venue-genre');;
            modalEditVenue.show();
        });
    });

    var modalDeleteVenue = new bootstrap.Modal(document.getElementById('modal-delete-venue'));
    document.querySelectorAll('.modal-trigger-delete-venue').forEach(function (button) {
        button.addEventListener('click', function () {
            var venueId = this.getAttribute('data-venue-id');
            document.getElementById('delete-venue-id').value = venueId;
            document.getElementById('title-delete-venue').textContent += this.getAttribute('data-venue-name');
            modalDeleteVenue.show();
        });
    });

    initializeSortableTable("locations", updateLocationsOrder);
});

function updateLocationsOrder() {
    saveScrollPosition();
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