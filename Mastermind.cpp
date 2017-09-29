#include <iostream>
#include <string>
#include <ctime>

using namespace std;

string getSecret(){
//enables a random secret each round
  srand((int)time(0));

  string secret = "";
  for (int x = 0; x < 5; x++) {
    secret = secret + to_string(rand() % 9 + 1);
  }
  return secret;
}
//recieves user input for their guesses
string getGuess(){
  string temp;

  cin >> temp;

  while(temp.length() != 5){
    cout << "Enter a FIVE digit number!" << endl;
    cin >> temp;
  }

  return temp;
}

//checks for if the guess is correct
string check(string guess, string secret) {
  for (int x = 0; x < 5; x++) {
    if (secret.at(x) == guess.at(x)) {
      guess[x] = '*';
    }
  }
  for (int x = 0; x < 5; x++) {
    for (int y = 0; y < 5; y++) {
      if (secret.at(x) == guess.at(y) and x != y) {
        guess[y] = '+';
      }
    }
  }
  for (int x = 0; x < 5; x++) {
    if (guess.at(x) != '*' and guess.at(x) != '+'){
      guess[x] = '-';
    }
  }

  return guess;
}


int main(){
  string secret = "";
  string guess = "";
  int count = 0;

  secret = getSecret();

  cout << "Enter a guess" << endl;
  //player continues to guess until they a) run out of chances b) are correct
  do {
    guess = getGuess();

    cout << " " << check(guess, secret) << endl;

    count++;
  } while (count < 5 and check(guess, secret) != "*****");

  //if the player runs out of guesses
  if (count == 5) {
    cout << "Sorry, the answer was " << secret << endl;
  } else {
    cout << "Nice!" << endl;
  }

  return 0;
}
