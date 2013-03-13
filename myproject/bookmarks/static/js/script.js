$(
    function(){
        $('#new-bookmark-widget form').on('submit', function(e){
            e.preventDefault();
            var inputs = $('#new-bookmark-widget input');
            var data = {};
            $.each(inputs, function(index){
                var input = inputs[index];
                data[input.name] = input.value;
            });
            $.ajax({
              type: "POST",
              url: '/',
              data: data,
              success: function(data){
                $('.error').hide();
                $('.bookmarks').prepend(data);
              }
            });
        });
    }
);
