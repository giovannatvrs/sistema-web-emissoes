import { Component, EventEmitter, Output } from '@angular/core';
import { Filtros } from '../../models/filtros';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-filtros-emissoes',
  imports: [FormsModule],
  templateUrl: './filtros-emissoes.html',
  styleUrl: './filtros-emissoes.css',
})
export class FiltrosEmissoes {
  filtros: Filtros = {
    tipo: '',
    emissor: '',
    min_value: null,
    max_value: null,
    inicial_date: null,
    final_date: null
  };

  @Output() aplicarFiltros = new EventEmitter<Filtros>();
  @Output() resetarOrdenacao = new EventEmitter<void>();

  mostrarBotaoLimpar = false;

  temFiltroAtivo(): boolean {
  return !!(
    this.filtros.tipo?.trim() ||
    this.filtros.emissor?.trim() ||
    this.filtros.min_value !== null ||
    this.filtros.max_value !== null ||
    this.filtros.inicial_date ||
    this.filtros.final_date
  );
}

  filtrarCampos(){
    if (!this.temFiltroAtivo()) return;
    this.aplicarFiltros.emit(this.filtros);
    this.mostrarBotaoLimpar = true;
  }

  limparFiltros(){
    this.filtros = {tipo: '', emissor: '', min_value: null, max_value: null, inicial_date: null, final_date: null};
    this.aplicarFiltros.emit(this.filtros);
    this.resetarOrdenacao.emit();
    this.mostrarBotaoLimpar = false;
  }

}
