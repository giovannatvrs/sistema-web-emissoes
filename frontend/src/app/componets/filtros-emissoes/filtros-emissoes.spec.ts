import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FiltrosEmissoes } from './filtros-emissoes';

describe('FiltrosEmissoes', () => {
  let component: FiltrosEmissoes;
  let fixture: ComponentFixture<FiltrosEmissoes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FiltrosEmissoes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FiltrosEmissoes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
