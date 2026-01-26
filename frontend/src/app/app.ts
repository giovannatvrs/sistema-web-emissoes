import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatPaginatorIntl } from '@angular/material/paginator';
import { getPortuguesePaginatorIntl } from './shared/mat-paginator-pt';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
  providers: [
  { provide: MatPaginatorIntl, useFactory: getPortuguesePaginatorIntl }
  ]
})
export class App {
  protected readonly title = signal('frontend');
}
