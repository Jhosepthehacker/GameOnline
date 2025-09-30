function game(){
  const readlineSync = require('readline-sync');
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

    const number = undefined;
    let trys = null;

    while (true){
      let answerOfUser = readlineSync.question("Adivina un número del 1 al 100");
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
    }
}
}
}

game();
