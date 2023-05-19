$(document).ready(function(){
    $('#id_add_image')[0].addEventListner('change', (Event)=> {
        let imageField = $('#id_sequel').parents(p);
        if (Event.target.checked) {
            imageField.show();
        }
        else {
            imageField.hide();
        }
    })
});