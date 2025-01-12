import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ButtonsModule } from '@progress/kendo-angular-buttons';
import { InputsModule } from '@progress/kendo-angular-inputs';
import { MapModule } from '@progress/kendo-angular-map';
import { AppComponent } from './app.component';


@NgModule({
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        MapModule,
        FormsModule,
        HttpClientModule,
        ButtonsModule,
        InputsModule
    ],
    declarations: [ AppComponent ],
    bootstrap: [ AppComponent ]
})

export class AppModule { }
