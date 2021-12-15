
function btnCart(productId, thisProp) {
    
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    

    data = {
        'product_id': productId,
        csrfmiddlewaretoken: csrftoken
    }

    $.ajax({

        url: 'http://127.0.0.1:8000/core/addToCart/',
        type: 'POST',
        data: data,
        beforeSend: function () {
            $(thisProp).prop('disabled', true);
        },
        success: function (response) {
            $("#cartlen").html(response['cartLength'])
            $(thisProp).prop('disabled', false);

            if (response['msg'] == '1') {
                $(thisProp).html('Already Carted')
            } else {
                $(thisProp).html('Carted')
            }
            
        },
    });
};
