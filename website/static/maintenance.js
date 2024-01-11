var defaultOptions = {
    ordering: false,
    paging: false,
    searching: false,
    info: false
}

var locationsTable = $('#locations');
var modal;
const modalId = 'modal'

$(document).ready(function () {
    modal = createModal(modalId);
    createLocationsTable();
    initializeSortableTable("locations", reorderLocations);
});

function createLocationsTable() {
    locationsTable.DataTable($.extend({}, defaultOptions, {
        ajax: "/maintenance/locations",
        columns: [
            { data: "name" },
            {
                data: null,
                defaultContent: '<i class="hoverable bi bi-pencil modal-trigger-edit"/>',
                width: "6%"
            },
            {
                data: null,
                defaultContent: '<i class="hoverable bi bi-trash modal-trigger-delete"/>',
                width: "6%"
            }
        ],
        createdRow: function (row, data, dataIndex) {
            $(row).attr('data-location-id', data.id); // need to store data id for drag and drop sorting - see reorderLocations()

            var editButton = $(row).find('.modal-trigger-edit');
            editButton.on('click', () => { showEditLocationModal(data); });

            var deleteButton = $(row).find('.modal-trigger-delete');
            deleteButton.on('click', () => { showDeleteLocationModal(data); });
        },
        drawCallback: () => {
            var hoverableElements = document.querySelectorAll('.hoverable');
            hoverableElements.forEach(changeFillOnHover);

            var addButton = $(locationsTable).find('.modal-trigger-add');
            addButton.on('click', () => { showAddLocationModal(); })
        }
    }));
}

function showAddLocationModal() {
    var form = createAddEditLocationForm();
    setModalContent(modalId, 'Add Location', form)
    modal.show();
}

function showEditLocationModal(locationData) {
    var form = createAddEditLocationForm(locationData);
    setModalContent(modalId, 'Edit Location', form)
    modal.show();
}

function createAddEditLocationForm(locationData) {
    var formContent = document.createElement('div');

    var idInput = document.createElement('input');
    idInput.type = 'hidden';
    idInput.name = 'id';
    formContent.appendChild(idInput);

    var nameLabel = document.createElement('label');
    nameLabel.for = 'location-name';
    nameLabel.className = 'form-label';
    nameLabel.innerText = 'Name';
    formContent.appendChild(nameLabel);

    var nameInput = document.createElement('input');
    nameInput.id = 'location-name';
    nameInput.type = 'text';
    nameInput.className = 'form-control';
    nameInput.name = 'name';
    nameInput.placeholder = 'Enter name';
    nameInput.required = true;
    formContent.appendChild(nameInput);

    if (locationData) {
        idInput.value = locationData.id;
        nameInput.value = locationData.name;
    }

    var submitText = locationData ? 'Save' : 'Add';
    var action = '/maintenance/' + (locationData ? 'edit-location' : 'add-location')

    return createModalForm('add-edit-location-form', action, submitText, formContent);
}

function showDeleteLocationModal(locationData) {
    var form = createDeleteLocationForm(locationData.id);
    setModalContent(modalId, `Delete Location: ${locationData.name}`, form);
    modal.show();
}

function createDeleteLocationForm(locationId) {
    var formContent = document.createElement('div');

    var idInput = document.createElement('input');
    idInput.type = 'hidden';
    idInput.name = 'id';
    idInput.value = locationId;
    formContent.appendChild(idInput);

    var message = document.createElement('p');
    message.innerText = 'Are you sure you want to delete this location?';
    formContent.appendChild(message);

    return createModalForm('delete-location-form', '', 'Yes', formContent);
}

function reorderLocations() {
    var order = $('#locations tbody').sortable('toArray', { attribute: 'data-location-id' });

    $.ajax({
        type: 'POST',
        url: '/maintenance/reorder-locations',
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

