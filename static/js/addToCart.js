


function btnCart(productId, thisProp) {
    
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    

    data = {
        'product_id': productId,
        csrfmiddlewaretoken: csrftoken
    }

    $.ajax({

        url: 'https://www.axivauniverse.com/core/addToCart/',
        type: 'POST',
        data: data,
        beforeSend: function () {
            $(thisProp).prop('disabled', true);
        },
        success: function (response) {
            $("[id=cartlen]").html(response['cartLength'])
            $(thisProp).prop('disabled', false);

            if (response['msg'] == '1') {
                $(thisProp).html('Already Carted')
            } else {
                $(thisProp).html('Carted')
            }
            if (response['cartLength'] >0  ){
                if ($(window).width() < 767){
                    $('#cartmob').fadeIn()
                    $("[id=cartlen]").html(response['cartLength'])
                }
            }
            
        },
    });
};

function btnCartTwo(productId, thisProp) { 
    
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    var quantitySIN = $('#input-quantity').val();
    
    data = {
        'productID': productId,
        csrfmiddlewaretoken: csrftoken,
        'quantitySIN':quantitySIN
    }
    $.ajax({
        url: 'https://www.axivauniverse.com/core/addOrUpdate/',
        type: 'POST',
        data: data,
        beforeSend: function () {
            $(thisProp).prop('disabled', true);
        },
        success: function (response) {
            $("[id=cartlen]").html(response['cartLength'])
            $(thisProp).prop('disabled', false);
                $(thisProp).html('Cart Updated')
            if (response['cartLength'] >0  ){
                if ($(window).width() < 767){
                    $('#cartmob').fadeIn()
                    $("[id=cartlen]").html(response['cartLength'])
                }
            }
        },
    });
};



