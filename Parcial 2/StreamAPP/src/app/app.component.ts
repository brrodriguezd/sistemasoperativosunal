import { Component } from '@angular/core';
import axios from 'axios';
import { Observable, Observer } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'StreamAPP';

  constructor() { 
  }
  
  valor: any[] = ["cargando", "cargando", "cargando"]

  funcion():any[]{
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => {
        this.valor = [response.data.bpi.USD.rate_float, response.data.bpi.GBP.rate_float, response.data.bpi.EUR.rate_float];
      })
      .catch(error => {
        return error;
      })
      .finally(() => {
        console.log(this.valor);
        return this.valor;
    })
    return this.valor;
  }

  dolar = new Observable<any>((observer: Observer<any>) => { 
    setInterval(() => observer.next(this.funcion()[0]), 1000);
  });

  libra = new Observable<any>((observer: Observer<any>) => { 
    setInterval(() => observer.next(this.funcion()[1]), 1000);
  });

  euro = new Observable<any>((observer: Observer<any>) => { 
    setInterval(() => observer.next(this.funcion()[2]), 1000);
  });
}