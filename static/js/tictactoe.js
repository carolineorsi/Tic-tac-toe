$(".grid-square")
    .mouseenter(
        function() {
            $(this).css("background", "#CCC");
        }
    )
    .mouseleave(
        function() {
            $(this).css("background", "white");
        }
    );

$(".grid-square")
    .click(
        function() {
            $(this).text("O");
        }
    );