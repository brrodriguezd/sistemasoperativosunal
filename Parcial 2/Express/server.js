const express = require("express")();
const httpServer = require("http").Server(express);
const io = require("socket.io")(httpServer, {  
    cors: { 
        origin: "http://localhost:4200",    
        methods: ["GET", "POST"] 
    }       
});

httpServer.listen(3000, () => {
    console.log('Server started!')
})

var squares = Array(9).fill(null);
xIsNext = true;
winner = null;

function getPlayer(player){
    if (player == 1){
        return 'X';
    }else if(player == 2){
        return 'O';
    }else{
        return 'Observador';
    }
}

function playerBool(x){
    if (x){
      return 'X'
    }
    return 'O'
  }
function roomCount(room){
    a = io.sockets.adapter.rooms.get(room).size
    if (!a) return 0;
    return a;
}

function calculateWinner(square){
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];
    for (let i = 0; i < lines.length; i ++){
      const [a, b, c] = lines[i];
      if (
        square[a] && //no null
        square[a] == square[b] &&
        square[b] == square[c]
      ){
        return square[a];
      }
    }
    return null;
}

io.on("connection", socket =>{
    socket.join('room');
    console.log('conectado');
    console.log(roomCount('room'));
    socket.emit("test", getPlayer(roomCount('room')));
    socket.on("move", idx =>{
        squares[idx] = playerBool(xIsNext)
        winner = calculateWinner(squares);
        xIsNext = !xIsNext;
        io.emit("moveconfirmation", squares);
        io.emit("nuevoturno", xIsNext);
        io.emit("ganador", winner);
    })
    socket.on("nuevojuego", () =>{
        squares.fill(null)
        xIsNext = true;
        winner = null;
        io.emit("moveconfirmation", squares);
        io.emit("nuevoturno", xIsNext);
        io.emit("ganador", winner);
    })

    socket.on("disconnect", ()=>{
        socket.leave('room')
        console.log('desconectado')
    })
});