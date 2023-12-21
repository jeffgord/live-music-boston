function initializeSortableTable(tableId, updateFunction) {
    $("#" + tableId + " tbody").sortable({
        helper: fixHelperModified,
        update: function (event, ui) {
            updateFunction();
        }
    }).disableSelection();
}

function fixHelperModified(e, tr) {
    var $originals = tr.children();
    var $helper = tr.clone();
    $helper.children().each(function (index) {
        $(this).width($originals.eq(index).width());
    });
    return $helper;
}