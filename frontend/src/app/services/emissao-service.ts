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

  getEmissoes(skip= 0, limit = 30, sortBy: string, order: string, filtros: any): Observable<EmissaoResponse>
  {



    let params = new HttpParams().set('skip', skip)
                                    .set('limit', limit)
                                    .set('sort_by', sortBy)
                                    .set('order', order);

    if (filtros.tipo) params = params.set('tipo', filtros.tipo);
    if (filtros.emissor) params = params.set('emissor', filtros.emissor);
    if (filtros.min_value) params = params.set('min_value', filtros.min_value);
    if (filtros.max_value) params = params.set('max_value', filtros.max_value);
    if (filtros.inicial_date) params = params.set('inicial_date', filtros.inicial_date);
    if (filtros.final_date) params = params.set('final_date', filtros.final_date);

    return this.http.get<EmissaoResponse>(this.url, {params})
  }
  
  editarEmissao(id: number, emissao: any): Observable<any>{
    return this.http.put(`${this.url}/${id}`, emissao)
  }
  

}
