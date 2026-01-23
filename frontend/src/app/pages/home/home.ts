import { Component } from '@angular/core';
import { TabelaEmissoes } from '../../components/tabela-emissoes/tabela-emissoes';

@Component({
  selector: 'app-home',
  imports: [TabelaEmissoes],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {

}
