

$(function () {
    $(".register-btn").click(function () {
        $(".box-outside").show();
        // console.log("...");
    });

    $(".icon-hebingxingzhuang").click(function () {
        $(".box-outside").hide();
    });

    $(".switch").click(function () {
        var boxInside = $(".box-inside");
        var boxInsideLeft = boxInside.css("left");
        var boxInsideInt = parseInt(boxInsideLeft);
        if (boxInsideInt === 0) {
            boxInside.animate({"left": -400})
        } else {
            boxInside.animate({"left": 0})
        }

    });
});