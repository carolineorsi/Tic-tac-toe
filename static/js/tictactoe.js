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

$(".start-game").click(function() {
    $(".grid-square").empty();
    }
);

function updateBoard(board) {
    for (i = 0; i < 10; i++) {
        if (isNaN(board[i])) {
            $('#square' + i).text(board[i]);
        }
    }
}