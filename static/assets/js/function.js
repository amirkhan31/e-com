console.log("working file");

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data:$(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response){
            console.log("comment saved to db");

             if(response.bool == true){
                $("#review-res").html("Review added sucessfully.")
                $(".hide-comment-form").hide()
                $(".add-review").hide()

                // do full review section part 3 

             }
        }
    })
})