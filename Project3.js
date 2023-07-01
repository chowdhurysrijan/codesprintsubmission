//Process flow: JS Debugger Terminal> cd 'Directory where Project3.js is installed'> node Project3.js

const weather = require('weather-js');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter the name of the city you wish to search: ', (city) => {
  weather.find({ search: city, degreeType: 'C' }, (err, result) => {
    if (err) {
      console.log(err);
      return;
    }
    
    if (result.length === 0) {
      console.log('City entered does not exist. Please execute the Program again.');
      rl.close();
      return;
    }

    console.log('Weather for:', result[0].location.name);
    console.log('Temperature Conditions:', result[0].current.temperature + '°C');
    console.log('Sky Conditions:', result[0].current.skytext);
    
    rl.close();
  });
});
