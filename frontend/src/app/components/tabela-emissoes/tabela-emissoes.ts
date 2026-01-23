import { Component, OnInit } from '@angular/core';
import { Emissao } from '../../models/emissao';
import { EmissaoService } from '../../services/emissao-service';
import { MatPaginatorModule, PageEvent, MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-tabela-emissoes',
  imports: [MatPaginator],
  templateUrl: './tabela-emissoes.html',
  styleUrl: './tabela-emissoes.css',
})
export class TabelaEmissoes implements OnInit {
  emissoes: Emissao[] = [];
  total_emissoes = 0;
  pageSize = 30;
  pageIndex = 0;


  constructor(private emissaoService:EmissaoService)
  {

  }

  ngOnInit(): void {
    this.mostrarEmissoes();
  }

  mostrarEmissoes(event?: PageEvent){
   if(event){
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
   }

    this.emissaoService.getEmissoes(this.pageSize * this.pageIndex, this.pageSize).subscribe(
      response => {
        this.emissoes = response.emissoes
        this.total_emissoes = response.total
    });
  }
  
}
