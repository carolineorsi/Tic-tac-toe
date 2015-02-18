$('#start-game').click(startGame);

function startGame(evt) {
    evt.preventDefault();

    $.get('/game',
          {'first-player': $('#first-player').val()},
          function(data) {
            console.log(data.message);
            showAlert(data.message);
            if (data.board) {
                updateBoard(data.board);
            };
          }
    );
}

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

// $(".grid-square")
//     .click(
//         function() {
//             $(this).text("O");
//         }
//     );


function updateBoard(board) {
    for (i = 0; i < 10; i++) {
        if (isNaN(board[i])) {
            $('#square' + i).text(board[i]);
        }
    }
}

function showAlert(message) {
    $("#message-alert").text(message);
    
    setTimeout(function(message) {
        $("#message-alert").empty();
    }, 3000);
}