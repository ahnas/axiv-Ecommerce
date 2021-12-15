$(document).ready(function(){
    $.ajax({

        url: 'http://127.0.0.1:8000/core/headerloader/',
        type: 'GET',
        
        
        success: function (response) {
            $("#cartlen").html(response['cartLength'])
   
        },
    });

});
    
