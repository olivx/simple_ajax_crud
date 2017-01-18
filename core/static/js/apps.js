$(function (){

    var loadForm =  function(){
        var btn = $(this);
        $.ajax({
            url:         btn.attr('data-url'),
            type:       'GET',
            dataType:   'json',
            beforeSend: function(){
                $('#modal-book').modal('show');
            },
            success: function(data){
                $('#modal-book .modal-content').html(data.html_form);
            }
        });
    };


    var saveForm = function(){
            var form = $(this);

            $.ajax({
                url:        form.attr('action'),
                type:       form.attr('method'),
                data:       form.serialize(),
                dataType:   'json',
                success:    function(data){
                    if (data.is_form_valid){
                        $('#book-table tbody').html(data.html_book_list);
                        $('#modal-book').modal('hide');
                    }else{
                        $('#modal-book .modal-content').html(data.html_form);
                    }

                }
            });
            return false;

    };


//  create book
    $('.js-create-book').click(loadForm);
    $('#modal-book').on('submit','.js-book-create-form' ,saveForm);

//  update book
    $('.js-update-book').click(loadForm);
    $('#modal-book').on('submit', '.js-book-update-form', saveForm);


});