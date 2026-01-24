import { Component, EventEmitter, Output } from '@angular/core';
import { Filtros } from '../../models/filtros';
import { FormsModule } from '@angular/forms';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { provideNativeDateAdapter } from '@angular/material/core';

@Component({
  selector: 'app-filtros-emissoes',
  imports: [MatDatepickerModule, FormsModule, MatFormFieldModule, MatInputModule],
  providers: [provideNativeDateAdapter()],
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

  filtrarCampos(){
    this.aplicarFiltros.emit(this.filtros);
  }

  limparFiltros(){
    this.filtros = {tipo: '', emissor: '', min_value: null, max_value: null, inicial_date: null, final_date: null};
    this.filtrarCampos();
  }

}
