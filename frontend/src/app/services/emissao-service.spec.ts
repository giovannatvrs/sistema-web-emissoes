import { TestBed } from '@angular/core/testing';

import { EmissaoService } from './emissao-service';

describe('EmissaoService', () => {
  let service: EmissaoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EmissaoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
