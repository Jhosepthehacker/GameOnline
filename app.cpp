#include <iostream>

// Proximamente se implementará "SDL2"

using namespace std;

namespace message {
  string hello = "Hola Usuario";
}

void game() {
  string name;
  
  cout << message:: hello << endl;
  cout << "\n";

  cout << "¿Cómo te llamas?: ";
  cin >> name;
  cout << "\n";
  
  cout << "Mucho gusto " + name << endl;
  
  int userPlaying;
  int number = 20; // Se está trabajando el problema del random (en desarrollo....)
  int trys = 0;

  while (true) {
    cout << "Adivina un número del 1 al 100: ";
    cin >> userPlaying;
    cout << "\n";

    if (userPlaying < number) {
      cout << "Demasiado bajo" << endl;
    }
    else if (userPlaying > number) {
      cout << "Demasiado alto" << endl;
    }
    else if (userPlaying == number) {
      cout << "Felicidades has encontrado el número " << number << " en " << trys << " intentos" << endl;
      break;
    }
  }
}

int main() {
  game();

  return 0;
}
