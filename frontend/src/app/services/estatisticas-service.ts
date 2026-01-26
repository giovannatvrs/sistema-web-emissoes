import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class EstatisticasService {
  private url = "http://127.0.0.1:8000/stats"
  constructor(private http: HttpClient)
  {

  }

  getStats(){
      return this.http.get<any>(this.url)
  }

  
}