$(document).ready(function() {
    $.ajax({
        url: "/get_categories",
        type: "GET",
        success: function(data) {
            $.each(data, function(index, category) {
                $('#category').append($('<option>', {
                    value: category.Categoryid,
                    text: category.Categoryid + " - " + category.Category
                }));
            });
        }
    });


    $('#category').change(function() {
        var category_id = $(this).val();
        $('#item').empty().append($('<option>', {
            value: "",
            text: "Select Item"
        }));


        $.ajax({
            url: "/get_items",
            type: "GET",
            data: {
                category_id: category_id
            },
            success: function(data) {
                $('#item').empty();


                $.each(data, function(index, item) {
                    $('#item').append($('<option>', {
                        value: item[0],
                        text: item[0]
                    }));
                });
            }
        });
    });


    $('#item').change(function() {
        var category_id = $('#category').val();
        var item_id = $(this).val();
        $.ajax({
            url: "/get_item_details",
            type: "GET",
            data: {
                category_id: category_id,
                item_id: item_id
            },
            success: function(data) {
                $('#brand_name').val(data.brand_name);
                $('#model_name').val(data.model_name);
                $('#specifications').val(data.specifications);
            }
        });
    });
});



