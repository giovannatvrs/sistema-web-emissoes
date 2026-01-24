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
  ordenacao = {coluna: "id", ordem: "asc"}

  constructor(private emissaoService:EmissaoService)
  {

  }

  ngOnInit(): void {
    this.mostrarEmissoes();
  }

  mostrarBotao = false;

  resetarOrdenacao(){
    this.ordenacao.coluna = 'id';
    this.ordenacao.ordem = 'asc';
    this.mostrarBotao = false;
    this.mostrarEmissoes();
  }

  ordernar(coluna: string){
    if(this.ordenacao.coluna === coluna){
      if(this.ordenacao.ordem === 'asc'){
          this.ordenacao.ordem = 'desc';
      }
      else{
          this.ordenacao.ordem = 'asc';
      }
       
    }else{
        this.ordenacao.coluna = coluna
        this.ordenacao.ordem = 'asc';
    }
    this.mostrarBotao = true;
    this.pageIndex = 0;
    this.mostrarEmissoes();
  }

  mostrarEmissoes(event?: PageEvent){
   if(event){
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
   }

    this.emissaoService.getEmissoes(this.pageSize * this.pageIndex, this.pageSize, this.ordenacao.coluna, this.ordenacao.ordem).subscribe(
      response => {
        this.emissoes = response.emissoes
        this.total_emissoes = response.total
    });
  }

  
  
}
