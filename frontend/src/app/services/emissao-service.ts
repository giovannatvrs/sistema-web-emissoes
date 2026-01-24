import { Injectable } from '@angular/core';
import { Emissao } from '../models/emissao';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface EmissaoResponse{
  emissoes: Emissao[],
  total: number,
  
}

@Injectable({
  providedIn: 'root',
})
export class EmissaoService {
  private url = "http://127.0.0.1:8000/emissoes";

  constructor(private http: HttpClient)
  {

  }

  getEmissoes(skip= 0, limit = 30, sortBy: string, order: string): Observable<EmissaoResponse>
  {
    const params = new HttpParams().set('skip', skip)
                                    .set('limit', limit)
                                    .set('sort_by', sortBy)
                                    .set('order', order);
    return this.http.get<EmissaoResponse>(this.url, {params})
  }
  

}
