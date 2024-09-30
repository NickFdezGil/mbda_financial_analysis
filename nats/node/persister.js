const { simulateDatabase } = require('./simulate');
const { random } = require('./random');

const persisterId = process.argv.length > 2 ? process.argv.slice(-1)[0] : random(1, 9);

const db = simulateDatabase(persisterId);

// Persister should get messages from queue and store them using `db.save` method
// After that, it should send back an ACK confirmation for that message.
// COMPLETE CODE HERE

// EXAMPLE 3. How to store a message in the database (simulated!)
const message = { id: 'A1' };
db.save(message).then(ack => {
  console.log('Message properly stored', ack);
  // COMPLETE CODE HERE
});
