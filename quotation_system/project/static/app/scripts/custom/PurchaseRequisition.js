    $('.add-field-input').on('change', function() {
    var numberOfFields = $(this).val();
    $('.items-container').empty();
    for(var i = 0; i < numberOfFields; i++) {
        $('.items-container').append(`
            <tr class="item-field">
                <td>
                    <label>Item Name</label>
                    <input type="text" name="pr_item_name" class="form-control item-name">
                </td>
                <td>
                    <label>Item Quantity</label>
                    <input type="number" name="pr_item_quantity" class="form-control item-quantity">
                </td>a
            </tr>
        `);
    }
});
document.getElementById("submit-button").addEventListener("click", function(event) {
    event.preventDefault();
    var form = document.getElementById("form");
    if(form.checkValidity()){
        $('#exampleModal').modal('show');
    } else {
        $('#errorModal').modal('show');
    }
});

