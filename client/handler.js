/**
 * Created by Cracker0 on 3/26/2017.
 */
function searchName()
{
    var name = document.getElementById("search").value;
    $("#ingredient").html("");


    $.getJSON("http://nginx/inventory/" + name,  function(data)
    {

        for (var i in data.items) {
            $('#ingredients_id').val(data.items[i].id);
            $('#ingredients_name').val(data.items[i].name);
            $('#ingredients_desc').val(data.items[i].description);
            $('#ingredients_amount').val(data.items[i].amount);
            $('#ingredients_alpha').val(data.items[i].alpha);
            $('#ingredients_date').val(data.items[i].date);
            $('#ingredients_type').val(data.items[i].type);
        }
    });
}