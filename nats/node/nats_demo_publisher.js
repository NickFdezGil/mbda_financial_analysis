const NATS = require('nats');
const nats = NATS.connect({ servers: ['nats://127.0.0.1:4222'] });

// EJEMPLO 1 Publicar un mensaje en JSON y después cerrar la conexión
const { random } = require('./random');
nats.publish('prices.daily', JSON.stringify({ MSFT: random(0, 100) }), () => {
  nats.close();
});

// EJEMPLO 2 Publicar dos mensajes en dos colas distintas y después cerrar la conexión
// nats.publish('foo.bar', `FIRST ${new Date().toISOString()}`, () => {
//   nats.publish('foo.yeah.thing', `SECOND ${new Date().toISOString()}`, () => {
//     nats.close();
//   });
// });
