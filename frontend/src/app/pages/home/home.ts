import { Component, OnInit } from '@angular/core';
import { TabelaEmissoes } from '../../components/tabela-emissoes/tabela-emissoes';
import { Emissao } from '../../models/emissao';
import { EmissaoService } from '../../services/emissao-service';
import { PageEvent } from '@angular/material/paginator';
import { FiltrosEmissoes } from '../../components/filtros-emissoes/filtros-emissoes';
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-home',
  imports: [TabelaEmissoes, FiltrosEmissoes, MatPaginator],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home implements OnInit{
  emissoes: Emissao[] = [];
  total_emissoes = 0;
  pageSize = 30;
  pageIndex = 0;
  ordenacao = {coluna: "id", ordem: "asc"}
  filtros: any = {};

  constructor(private emissaoService:EmissaoService)
  {

  }

  ngOnInit(): void {
    this.mostrarEmissoes();
  }

  obterFiltros(filtrosEmissoesEvent: any){
    this.filtros = filtrosEmissoesEvent;
    this.pageIndex = 0;
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

    this.emissaoService.getEmissoes(this.pageSize * this.pageIndex, this.pageSize, this.ordenacao.coluna, this.ordenacao.ordem, this.filtros).subscribe(
      response => {
        this.emissoes = response.emissoes
        this.total_emissoes = response.total
    });
  }

}
