import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { faChartLine } from '@fortawesome/free-solid-svg-icons';
import { faHome } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-barra-lateral',
  imports: [RouterLink, FontAwesomeModule],
  templateUrl: './barra-lateral.html',
  styleUrl: './barra-lateral.css',
})
export class BarraLateral {
  faChartLine = faChartLine;
  faHome = faHome;

  constructor(public router: Router) {}

  isDashboard(): boolean {
    return this.router.url === '/dashboard';
  }
}
