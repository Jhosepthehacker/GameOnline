#include <iostream>

// Proximamente se implementará "SDL2"

namespace message {
  std:: string hello = "Hola Usuario";
}

void game() {
  std:: string name;
  
  std:: cout << message:: hello << std:: endl;
  std:: cout << "\n";

  std:: cout << "¿Cómo te llamas?: ";
  std:: cin >> name;
  std:: cout << "\n";
  
  std:: cout << "Mucho gusto " + name << std:: endl;
  
  int userPlaying;
  int number = 20; // Se está trabajando el problema del random (en desarrollo....)
  int trys = 0;

  while (true) {
    std:: cout << "Adivina un número del 1 al 100: ";
    std:: cin >> userPlaying;
    std:: cout << "\n";

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
