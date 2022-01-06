$(document).ready(function(){
    
    $.ajax({

        url: 'https://www.axivauniverse.com/core/headerloader/',
        type: 'GET',
        
        
        success: function (response) {
            $("[id=cartlen]").html(response['cartLength'])

            if (response['cartLength'] >0  ){
                if ($(window).width() < 767){

                    $('#cartmob').fadeIn()
                    $("[id=cartlen]").html(response['cartLength'])
                    
                }
            }
   
        },
    });

});
    
