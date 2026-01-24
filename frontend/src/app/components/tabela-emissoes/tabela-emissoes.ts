import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Emissao } from '../../models/emissao';


@Component({
  selector: 'app-tabela-emissoes',
  imports: [],
  templateUrl: './tabela-emissoes.html',
  styleUrl: './tabela-emissoes.css',
})
export class TabelaEmissoes {
  
  @Input() emissoes: Emissao[] = [];
  @Input() ordenacao: any = {coluna: 'id', ordem: 'asc'};
  @Output() ordenar = new EventEmitter<any>();

  
  ordernar(coluna: string) {
    let ordem = 'asc';
    if (this.ordenacao.coluna === coluna) {
      ordem = this.ordenacao.ordem === 'asc' ? 'desc' : 'asc';
    }
    this.ordenar.emit({ coluna, ordem });
  }

  resetarOrdenacao(){
    this.ordenar.emit({coluna: 'id', ordem: 'asc' });
  }
 
  
}
