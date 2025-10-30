game = () => {
  const readlineSync = require('readline-sync');
  const Random = require('random-js').Random;
  const random = new Random();
  
  const messageWarning = "¡Si no usas CommonJs, no podrás interactuar con este juego!";

  console.log(messageWarning);
  console.log("");

  const userName = readlineSync.question("¿Cómo te llamas?: ");
  console.log(`¡Qué bonito nombre ${userName}!`);
  console.log("");

  const questionForTheUser = readlineSync.question("¿Quiéres jugar a adivinar un número del 1 al 100?: ")

  // Se comprueban dos 'si', uno con acento y otro sin acento (para aclarar la confusión en caso de que si la hay)

  if (questionForTheUser === "sí" || questionForTheUser === "si"){
    console.log("Empezando el juego....");

    const number = random.integer(1, 100); // Próximamente se reemplazará "random-js" y se usará "Math.floor()" y "Math.random()" (recomendado).
    let trys = 0;

    while (true){
      let answerOfUser = readlineSync.question("Adivina un número del 1 al 100: ");
      trys += 1;
    
      console.log("");
    
      if (answerOfUser > number){
        console.log(`El número ${answerOfUser} es demasiado alto`);
    }
      else if (answerOfUser < number){
        console.log(`El número ${answerOfUser} es demasiado bajo`);
    }
      else if (answerOfUser === number){
        console.log(`Felicidades has encontrado el número ${answerOfUser}, en ${trys} intentos`);
        console.log("");

        const levelUpGame = readline.question(`${userName} deseas subir la dificultad: `);
        const notSpaces = 0;
        
        for (let i = 0; i < levelUpGame.length; i++) {
          if (levelUpGame[i] != " ") {
            
          }
        }
    }
  }
 }
}

game();
