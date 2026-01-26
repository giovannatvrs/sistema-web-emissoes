import { Component, OnInit, HostListener } from '@angular/core';
import { BarraLateral } from '../../components/barra-lateral/barra-lateral';
import { CommonModule } from '@angular/common';
import { EstatisticasService } from '../../services/estatisticas-service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, BarraLateral],
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class Dashboard implements OnInit {
  public stats: any;
  public graficosProntos = false;
  private nomesMeses = ['', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];

  constructor(private statsService: EstatisticasService) {}

  @HostListener('window:resize')
  onResize() {
    if (this.graficosProntos) {
      this.drawCharts();
    }
  }

  ngOnInit() {
    this.graficosProntos = false;
    this.statsService.getStats().subscribe(data => {
      this.stats = data;
      this.graficosProntos = true;
      setTimeout(() => this.iniciarGoogleCharts(), 150);
    });
  }

  iniciarGoogleCharts() {
    const google = (window as any).google;
    if (google && google.visualization && google.visualization.DataTable) {
      this.drawCharts();
    } else {
      google.charts.load('current', { packages: ['corechart'], language: 'pt-BR' });
      google.charts.setOnLoadCallback(() => this.drawCharts());
    }
  }

  drawCharts() {
    if (!this.stats) return;

    const commonOptions = {
      height: 350,
      width: '100%',
      titleTextStyle: { fontSize: 20, color: '#002d6e', bold: true },
      chartArea: { width: '85%', height: '70%' },
      legend: { position: 'bottom' }
    };

    const barraData = (window as any).google.visualization.arrayToDataTable([
      ['Mês', 'Volume'],
      ...this.stats.volume_por_ano_mes.map((i: any) => [this.nomesMeses[i.mes], i.valor_total])
    ]);

    const pizzaData = (window as any).google.visualization.arrayToDataTable([
      ['Tipo', 'Valor'],
      ...this.stats.volume_por_tipo.map((t: any) => [t.tipo, t.valor_total])
    ]);

    const qtdData = (window as any).google.visualization.arrayToDataTable([
      ['Mês', 'Qtd'],
      ...this.stats.qtd_emissoes_por_ano_mes.map((m: any) => [this.nomesMeses[m.mes], m.qtd_emissoes])
    ]);

    const barraChart = new (window as any).google.visualization.ColumnChart(document.getElementById('barra_div'));
    barraChart.draw(barraData, { ...commonOptions, title: 'VOLUME MENSAL (R$)', colors: ['#002d6e'], legend: 'none' });

    const pizzaChart = new (window as any).google.visualization.PieChart(document.getElementById('pizza_div'));
    pizzaChart.draw(pizzaData, { ...commonOptions, title: 'DISTRIBUIÇÃO POR ATIVO', pieHole: 0.4 });

    const qtdChart = new (window as any).google.visualization.AreaChart(document.getElementById('qtd_div'));
    qtdChart.draw(qtdData, { ...commonOptions, title: 'QUANTIDADE DE OPERAÇÕES', colors: ['#20c997'], areaOpacity: 0.1 });
  }
}