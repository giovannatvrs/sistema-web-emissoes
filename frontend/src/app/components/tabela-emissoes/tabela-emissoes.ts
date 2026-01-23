import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tabela-emissoes',
  imports: [],
  templateUrl: './tabela-emissoes.html',
  styleUrl: './tabela-emissoes.css',
})
export class TabelaEmissoes implements OnInit {
  emissaoList: any[]=[];

  constructor(private http: HttpClient)
  {

  }

  ngOnInit(): void {
    this.getEmissoes();
  }

  getEmissoes()
  {
    this.http.get("http://127.0.0.1:8000/emissoes").subscribe((result: any) =>
      {
        this.emissaoList = result;
      }
    )
  }
}
