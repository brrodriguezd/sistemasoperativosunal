import { Component, OnInit } from '@angular/core';
import { io } from 'socket.io-client';

@Component({ 
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'Triqui';
  winner: any;
  private player: any;
  private socket: any;
  private xIsNext!: boolean;
  squares: any[] = Array(9).fill(null)

  newGame(){
    this.socket.emit("nuevojuego", )
  }
  //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

  ngOnInit(): void {
    this.socket = io("http://localhost:3000")

    this.socket.on("test", (player: any) => {
      this.player = player;
      this.xIsNext = true;
      this.winner = null;
    })
  }

  playerBool(x:any){
    if (x == 'X'){
      return true
    }else if(x == 'O'){
      return false;
    }else{
      return null;
    }
  }
  makeMove(idx: number){
    if (!this.squares[idx] && !this.winner && this.xIsNext == this.playerBool(this.player)){
      this.socket.emit("move", idx)
    }  
  }

  get x(){
    return this.player;
  }

  get turno(){
    if(this.xIsNext){
      return 'X';
    }else{
      return 'O';
    }
  }
  ngAfterViewInit(){
    this.socket.on("moveconfirmation", (squares: any[]) =>{
      this.squares = squares;
    })
    this.socket.on("nuevoturno", (x: boolean) =>{
      this.xIsNext = x;
    })
    this.socket.on("ganador", (winner :any) =>{
      this.winner = winner;
    })
  }
}
