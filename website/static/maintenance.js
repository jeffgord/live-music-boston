document.addEventListener('DOMContentLoaded', function () {
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
            var locationId = this.getAttribute('data-location-id');
            document.getElementById('add-select-venue-location').value = `${locationId}`;
            modalAddVenue.show();
        });
    });

    var modalEditVenue = new bootstrap.Modal(document.getElementById('modal-edit-venue'));
    document.querySelectorAll('.modal-trigger-edit-venue').forEach(function (button) {
        button.addEventListener('click', function () {
            var locationId = this.getAttribute('data-venue-location-id');
            document.getElementById('edit-select-venue-location').value = `${locationId}`;
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
});