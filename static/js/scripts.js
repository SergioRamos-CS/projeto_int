document.addEventListener('DOMContentLoaded', function() {
    // Máscara para CNPJ
    const cnpjField = document.getElementById('id_cnpj');
    if (cnpjField) {
        IMask(cnpjField, {
            mask: '00.000.000/0000-00',
            prepare: function (value) {
                return value.replace(/\D/g, '');
            }
        });
    }

    // Máscara para Telefone
    const telefoneField = document.getElementById('id_telefone');
    if (telefoneField) {
        IMask(telefoneField, {
            mask: '(00) 00000-0000',
            prepare: function (value) {
                return value.replace(/\D/g, '');
            }
        });
    }

});