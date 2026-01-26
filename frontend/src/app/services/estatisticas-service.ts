import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environment/environment';
@Injectable({
  providedIn: 'root',
})
export class EstatisticasService {
  private url = `${environment.apiUrl}/stats`
  constructor(private http: HttpClient)
  {

  }

  getStats(){
      return this.http.get<any>(this.url)
  }

  
}