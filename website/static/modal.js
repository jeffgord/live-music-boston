function createModal(id) {
    return new bootstrap.Modal(document.getElementById(id));
}

function setModalContent(id, title, bodyContent) {
    var titleElement = document.getElementById(`${id}-title`);
    titleElement.innerText = title;

    var modalBody = document.getElementById(`${id}-body`);
    modalBody.replaceChildren();
    modalBody.appendChild(bodyContent);
}

function createModalForm(action, submitText, formContent) {
    var form = document.createElement('form');
    form.id = 'modal-form';
    form.action = action;
    form.method = 'POST';

    form.appendChild(formContent);
    form.appendChild(document.createElement('br'));

    var buttonWrapper = document.createElement('div');
    buttonWrapper.style = 'text-align: right;';
    form.appendChild(buttonWrapper);

    var submitButton = document.createElement('button');
    submitButton.type = 'button';
    submitButton.className = 'btn btn-secondary btn-form';
    submitButton.innerText = submitText;
    submitButton.on('click', () => { submitModalForm(form.id); });
    buttonWrapper.appendChild(submitButton);

    return form;
}

function submitModalForm(formId) {
    var form = $(`#${formId}`);

    $.ajax({
        type: 'POST',
        url: form[0].action,
        data: form.serialize()
    })
}