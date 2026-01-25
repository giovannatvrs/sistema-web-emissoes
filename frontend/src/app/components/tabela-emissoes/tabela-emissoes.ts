import { Component, EventEmitter, inject, Input, OnInit, Output } from '@angular/core';
import { Emissao } from '../../models/emissao';
import { CommonModule } from '@angular/common';
import { EditModal } from '../edit-modal/edit-modal';
import { EmissaoService } from '../../services/emissao-service';
@Component({
  selector: 'app-tabela-emissoes',
  imports: [CommonModule, EditModal],
  templateUrl: './tabela-emissoes.html',
  styleUrl: './tabela-emissoes.css',
})
export class TabelaEmissoes {
  private emissaoService = inject(EmissaoService);
  @Input() emissoes: Emissao[] = [];
  @Input() ordenacao: any = {coluna: 'id', ordem: 'asc'};
  @Output() ordenar = new EventEmitter<any>();
  @Output() atualizarDados = new EventEmitter<any>();

  exibirModal = false;
  emissaoSelecionada: any = null;
  

  
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

  
  mostrarModal(emissao: any){
    this.emissaoSelecionada = {...emissao};
    this.exibirModal = true;
  }

  salvarEdicao(dadosEditados: any) {
    this.emissaoService.editarEmissao(dadosEditados.id, dadosEditados).subscribe({
      next: () => {
        this.exibirModal = false;
        this.atualizarDados.emit(); 
      },
      error: (err) => {
        console.error("Erro ao salvar:", err);
        alert("Erro ao atualizar emissão.");
      }
    });
  }





}