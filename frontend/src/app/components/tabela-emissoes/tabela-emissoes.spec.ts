import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TabelaEmissoes } from './tabela-emissoes';

describe('TabelaEmissoes', () => {
  let component: TabelaEmissoes;
  let fixture: ComponentFixture<TabelaEmissoes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TabelaEmissoes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TabelaEmissoes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
