const SerialPort = require('serialport');
const port = new SerialPort('COM3', { baudRate: 9600 }); // Remplace 'COM3' avec ton port série

port.on('open', () => {
  console.log('Port série ouvert');
});

port.on('data', (data) => {
  console.log('Données reçues :', data.toString());
});

port.on('error', (err) => {
  console.error('Erreur série:', err);
});
