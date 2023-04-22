$(document).ready(function () {
    $('.add-favorite').on('click', function () {
        let pk = $(this).data('post');
        $.ajax({
            url: '/api/favorite/' + pk + '/',
            type: 'POST',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function (data) {
                if (data.status === 'added') {
                    $('.add-favorite[data-post=' + pk + ']').addClass('active');
                } else {
                    $('.add-favorite[data-post=' + pk + ']').removeClass('active');
                }
            }
        });
    });
});

