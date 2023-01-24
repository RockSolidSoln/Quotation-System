    $('.add-field-input').on('change', function() {
    var numberOfFields = $(this).val();
    $('.items-container').empty();
    for(var i = 0; i < numberOfFields; i++) {
        $('.items-container').append(`
            <tr class="item-field">
                <td>
                    <label>Item Name</label>
                    <input type="text" name="q_item_name" class="form-control item-name">
                </td>
                <td>
                    <label>Item Quantity</label>
                    <input type="number" name="q_item_quantity" class="form-control item-quantity">
                </td>a
                <td>
                    <label>Item Price</label>
                    <input type="number" name="q_item_price" class="form-control item-price">
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
document.getElementById("inputGroupSelect01").addEventListener("change", updateCustomerId);

function updateCustomerId() {
        var pr_id = document.getElementById("inputGroupSelect01").value;
        console.log(pr_id);
        $.ajax({
          type: 'GET',
          url: '/get_customer_id/',
          data: {
            'pr_id': pr_id
          },
          success: function (data) {
            document.getElementById("customer_id").value = data.customer_id;
        }
        });
        console.log("Data tried")
    }
document.getElementById("submit-button").addEventListener("click", function(event) {
    event.preventDefault();
    const form = document.getElementById("form");
    let isValid = true;
    for (let i = 0; i < form.elements.length; i++) {
        if(!form.elements[i].validity.valid){
            isValid = false;
            break;
        }
    }
    if(isValid){
        $('#exampleModal').modal('show');
    }
});
document.getElementById("form").addEventListener("invalid", function() {
    $('#errorModal').modal('show');
}, true);

