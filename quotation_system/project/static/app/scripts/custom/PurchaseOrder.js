    $('.add-field-input').on('change', function() {
    var numberOfFields = $(this).val();
    $('.items-container').empty();
    for(var i = 0; i < numberOfFields; i++) {
        $('.items-container').append(`
            <tr class="item-field">
                <td>
                    <label>Item Name</label>
                    <input type="text" name="po_item_name" class="form-control item-name">
                </td>
                <td>
                    <label>Item Quantity</label>
                    <input type="number" name="po_item_quantity" class="form-control item-quantity">
                </td>a
                <td>
                    <label>Item Price</label>
                    <input type="number" name="po_item_price" class="form-control item-price">
                </td>
            </tr>
        `);
    }
});

$(document).on('input', '.item-price', function() {
    let totalPrice = 0;
    $('.item-field').each(function() {
        const itemPrice = parseFloat($(this).find('.item-price').val());
        var itemQuantity = parseFloat($(this).find('.item-quantity').val());
        totalPrice += itemPrice * itemQuantity;
    });
    $('.total_price').val(totalPrice);
});
document.getElementById("inputGroupSelect02").addEventListener("change", updateCustomerId);

function updateId() {
        var quotation_id = document.getElementById("inputGroupSelect02").value;

        $.ajax({
          type: 'GET',
          url: '/customer_id/',
          data: {
            'quotation_id': quotation_id
          },
          success: function (data) {
            document.getElementById("customer_id").value = data.customer_id;
        }
        });
        $.ajax({
          type: 'GET',
          url: '/salesman_id/',
          data: {
            'quotation_id': quotation_id
          },
          success: function (data) {
            document.getElementById("salesman_id").value = data.salesman_id;
        }
        });
        console.log("Data tried")
    }

document.getElementById("submit-button").addEventListener("click", function(event) {
    var form = document.getElementById("form");
    if(form.checkValidity()){
        $('#exampleModal').modal('show');
    } else {
        $('#errorModal').modal('show');
    }
});

