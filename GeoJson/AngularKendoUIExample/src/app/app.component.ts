import { Component } from '@angular/core';
import { geoJson  } from './countries-users-india.geo';
import { ShapeCreatedEvent } from '@progress/kendo-angular-map';

@Component({
    selector: "my-app",
    template: `
      <kendo-map [center]="[40, 0]" (shapeCreated)="onShapeCreated($event)">
        <kendo-map-layers>
          <kendo-map-shape-layer
            [data]="data"
            [style]="{ fill: { color: 'green' } }"
          >
          </kendo-map-shape-layer>
        </kendo-map-layers>
      </kendo-map>
    `,
  })
export class AppComponent {
    data = geoJson;
    onShapeCreated(e: ShapeCreatedEvent): void {
        const shape = e.shape;
        const users = e.dataItem.properties.users;
        if (users) {
          const opacity = users / 1000;
          shape.options.set("fill.opacity", opacity);
        }
      }
}
