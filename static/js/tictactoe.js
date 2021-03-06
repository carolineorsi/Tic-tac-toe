
$('#start-game').click(startGame);

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
            if (addO(($(this)))) {
                makePlay();
            }
        }
    );


function startGame(evt) {
    clearBoard();

    $.get('/start',
          {'first-player': $('#first-player').val()},
          function(data) {
            showAlert(data.message);
            if (data.board) {
                updateBoard(data.board);
            };
          }
    );
};


function addO(square) {
    if (square.text() === 'X' || $(this).text() === 'O') {
        showAlert("Invalid move. Choose another square.")
        return false;
    } 
    else {
        showAlert("");
        square.text("O");
        return true;
    }
};


function makePlay() {
    var board = getBoardState();

    $.get('/game',
      {'board': board},
      function(data) {
        showAlert(data.message);
        // if (data.board) {
        //     updateBoard(data.board);
        // };
      }
    );

};


function getBoardState() {
    var board = []

    for (i = 0; i < 10; i++) {
        var squareVal = $("#square" + i).text(); 
        if (isNaN(squareVal)) {
            board.push(squareVal);
        }
        else {
            board.push(i);
        }
    }

    return board;
};


function updateBoard(board) {
    for (i = 0; i < 10; i++) {
        if (isNaN(board[i])) {
            $('#square' + i).text(board[i]);

        }
    }
};


function clearBoard() {
    for (i = 0; i < 10; i++) {
        $('#square' + i).empty();
    }
};


function showAlert(message) {
    $("#message-alert").empty(message);
    $("#message-alert").text(message);

    // setTimeout(function(message) {
    //     $("#message-alert").empty();
    // }, 3000);
};





var model = {
    init: function() {
        this.board = [0,1,2,3,4,5,6,7,8]
        this.players = {'X': null, 'O': null}
    },

    getBoard: function() {
        return this.board;
    },

    getPlayerO: function() {
        return this.players['O'];
    },

    getPlayerX: function() {
        return this.players['X'];
    }
};

var gameControlView = {
    init: function() {
        this.firstPlayer = $("#first-player");
        this.startGame = $("#start-game");

        this.startGame.click(function() {
            // Call function in controller, passing in firstPlayer value
        });
    }
};

var gameBoardView = {
    init: function() {

    }
};

var messageView = {
    
}