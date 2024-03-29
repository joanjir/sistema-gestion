$(function () {
    $('#data').DataTable({
        scrollX: true,
        autoWidth: true,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [ 
        {"data": "ename"},
        {"data": "eapellido"},
        {"data": "eedad"},
        {"data": "egrupo"},
        {"data": "Anno_Academic"},
        {"data": "emilitancia"},
        {"data": "eautoevaluacion"},
        {"data": "evaluacion"},
        {"data": "id"},
        ],
        columnDefs: [{
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="/sgfeufac2.uci.cu/evaluaciones/editar/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                buttons += '<a href="/sgfeufac2.uci.cu/evaluaciones/eliminar/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                return buttons;
            }
        },],
        initComplete: function (settings, json) {

        }
    });
});