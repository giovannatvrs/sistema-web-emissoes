import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Dashboard } from './pages/dashboard/dashboard';

export const routes: Routes = [
    {path: 'home', component: Home, title: 'Página Inicial'},
    {path: 'dashboard', component: Dashboard, title: 'Dashboard'}
];
