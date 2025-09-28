function game(){
const messageWarning = "¡Si no usas CommonJs, no podrás interactuar con este juego!";

console.log(messageHello);
console.log("");

const userResponse = prompt("¿Cómo te llamas?: ");
console.log(`¡Qué bonito nombre ${userResponse}`);
console.log("");

const questionForTheUser = prompt("¿Quiéres jugar a adivinar un número del 1 al 100?: ")

// Se comprueban dos 'si', uno con acento y otro sin acento (para aclarar la confusión en caso de que si la hay)

if (questionForTheUser === "sí" || questionForTheUser === "si"){
  console.log("Empezando el juego....");

  while true{
    const answerOfUser = promp();
}
}
}

game();
