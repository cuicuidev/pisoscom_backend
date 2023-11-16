# API para el modelo de pisoscom

Esta API está contenedorizada y permite hacer requests al endpoint "/predict" mediante el método POST. Si los datos proporcionados son válidos, la respuesta retornará una predicción del precio hecha por el modelo.

El payload del post debe seguir el siguiente formato:

```json
{
  "province": "string",
  "lat": 0.0,
  "lng": 0.0,
  "n_bathrooms": 0,
  "n_rooms": 0,
  "surface": 0.0,
  "net_surface": 0.0,
  "garden": true,
  "elevator": true,
  "garage": true,
  "condition": "string",
  "age": 0.0
}
```