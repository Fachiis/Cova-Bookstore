function payWithPaystack(){
    var handler = PaystackPop.setup({
      key: 'pk_test_fc2bac4f965d2af61ee57d3ca669f63e479bb62c',
      email: '{{ user.email }}',
      amount: {{ book.price }} * 100.00,
      currency: 'NGN',
      metadata: {
         custom_fields: [
            {
                display_name: "Mobile Number",
                variable_name: "mobile_number",
            }
         ]
      },
      callback: function(response){
          alert('Payment complete! Reference: ' + response.reference);
      },
      onClose: function(){
          alert('window closed');
      }
    });
    handler.openIframe();
  }


function upload_img(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img_id').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    };
  };