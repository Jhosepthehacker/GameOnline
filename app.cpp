#include <iostream>

void game() {
  int userPlaying;
  int number = 20;
  int trys = 0;

  while (true) {
    std:: cout << "Adivina un número del 1 al 100: ";
    std:: cin >> userPlaying;

    if (userPlaying < number) {
      std:: cout << "Demasiado bajo" << std:: endl;
    }
    else if (userPlaying > number) {
      std:: cout << "Demasiado alto" << std:: endl;
    }
    else if (userPlaying == number) {
      std:: cout << "Felicidades has encontrado el número " << number << " en " << trys << " intentos" << std:: endl;
      break;
    }
  }
}

int main() {
  game();

  return 0;
}
