import { Component, EventEmitter, Output, Input} from '@angular/core';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-edit-modal',
  imports: [FormsModule],
  templateUrl: './edit-modal.html',
  styleUrl: './edit-modal.css',
})
export class EditModal {
  @Input() emissao: any;
  @Output() fechar = new EventEmitter<void>();
  @Output() salvar = new EventEmitter<any>();

  ocultar(){
    this.fechar.emit();
  }

  confirmarEdicaoEmissao(){
    this.salvar.emit(this.emissao);
  }
}
