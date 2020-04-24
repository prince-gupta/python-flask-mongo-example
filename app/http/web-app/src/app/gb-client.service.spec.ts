import { TestBed } from '@angular/core/testing';

import { GbClientService } from './gb-client.service';

describe('GbClientService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GbClientService = TestBed.get(GbClientService);
    expect(service).toBeTruthy();
  });
});
