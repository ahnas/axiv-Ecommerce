$(document).ready(function(){
    
    $.ajax({

        url: 'http://127.0.0.1:8000/core/headerloader/',
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
    
