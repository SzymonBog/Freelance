#include <iostream>
#include <string.h>
#include <Windows.h>
#include <stdlib.h>
#include <time.h>
#include <cctype>
#include <string>

using namespace std;

void drawHangman(int chances)
{
	switch (chances)
	{
	case 10:
		cout << "";
		break;
	case 9:
		cout << "\n\n\n\n\n\n__________";
		break;
	case 8:
		cout << "|\n|\n|\n|\n|\n|__________";
		break;
	case 7:
		cout << "__________\n|\n|\n|\n|\n|\n|__________";
		break;
	case 6:
		cout << "__________\n|         |\n|\n|\n|\n|\n|__________";
		break;
	case 5:
		cout << "__________\n|         |\n|         0\n|\n|\n|\n|__________";
		break;
	case 4:
		cout << "__________\n|         |\n|         0\n|         |\n|\n|\n|__________";
		break;
	case 3:
		cout << "__________\n|         |\n|         0\n|        /|\n|\n|\n|__________";
		break;
	case 2:
		cout << "__________\n|         |\n|         0\n|        /|\\\n|\n|\n|__________";
		break;
	case 1:
		cout << "__________\n|         |\n|         0\n|        /|\\\n|        /\n|\n|__________";
		break;
	case 0:
		cout << "__________\n|         |\n|         0\n|        /|\\\n|        /\\\n|\n|__________";
		break;
	}
}

int wynik[2] = {0, 0};

void mainGame2(string password, char p)
{
	if (p == '1') {
		cout << "Player 2 gueses\n";
	}
	else {
		cout << "Player 1 gueses\n";
	}

	for (int i = 0; i < password.length(); i++) {
		if (isspace(password.at(i))) {
			cout << "  ";
		}
		else {
			cout << "_ ";
		}
	}
	cout << "\n";

	int chances = 10;
	string usedLetters;
	char letter;
	string goodLetters;
	bool win = false;

	while (chances != 0) {
		cin >> letter;

		bool result = false;
		// Check if string contains the character or not
		for (auto& elem : usedLetters)
		{
			if (elem == letter)
			{
				result = true;
				cout << "Letter " << letter << " has already been used\n";
				break;
			}
		}
		bool isInPassword = false;
		if (result == false) {
			for (auto& elem : password)
			{
				if (elem == letter)
				{
					isInPassword = true;
					goodLetters = goodLetters + letter;
				}
			}
			if (isInPassword == true) {
				for (auto& elemp : password)
				{
					if (isspace(elemp)) {
						cout << "  ";
					}
					else {
						bool res = false;
						for (auto& elemg : goodLetters)
						{
							if (elemg == elemp) {
								cout << elemp << " ";
								res = true;
								break;
							}
						}
						if (res == false) {
							cout << "_ ";
						}
					}
				}
			}
			else {
				usedLetters = usedLetters + letter;
				chances--;
			}
		}
		Sleep(1000);
		system("cls");
		drawHangman(chances);
		cout << endl;
		for (auto& elemp : password)
		{
			if (isspace(elemp)) {
				cout << "  ";
			}
			else {
				bool res = false;
				for (auto& elemg : goodLetters)
				{
					if (elemg == elemp) {
						cout << elemp << " ";
						res = true;
						break;
					}
				}
				if (res == false) {
					cout << "_ ";
				}
			}
		}
		cout << "\nUsed letters: ";
		for (auto& elem : usedLetters) {
			cout << elem << ", ";
		}
		cout << "\n";

		int guessedLettersCount = 0;
		int spaceCount = 0;
		for (auto& elemp : password)
		{
			if (isspace(elemp)) {
				spaceCount++;
			}
			else {
				for (auto& elemg : goodLetters)
				{
					if (elemg == elemp) {
						guessedLettersCount++;
						break;
					}
				}
				if (guessedLettersCount == password.length() - spaceCount) {
					switch (p) {
						case '1':
							wynik[1]++;
							break;
						case '2':
							wynik[0]++;
							break;
					}
					cout << "Player "<<p<< " won\nCurrent score is: "<<wynik[0]<<" : " << wynik[1]<< "\nGoing to main menu\n";
					chances = 0;
					win = true;
					Sleep(3000);
					system("cls");
				}
			}
		}
	}
	if (win == false) {
		switch (p) {
			case '1':
				wynik[0]++;
				break;
			case '2':
				wynik[1]++;
				break;
		}
		cout << "Player " << p << " won\nCurrent score is: " << wynik[0] << " : " << wynik[1] << "\n The password was: " << password << "\n Going to main menu";
		Sleep(5000);
		system("cls");
	}
}

void mainGame(string password, string kategoria)
{
	cout << "\nkategoria: " << kategoria<<"\n";
	for (int i = 0; i < password.length(); i++) {
		if (isspace(password.at(i))) {
			cout << "  ";
		}
		else {
			cout << "_ ";
		}
	}
	cout << "\n";

	int chances = 10;
	string usedLetters;
	char letter;
	string goodLetters;
	bool win = false;

	while (chances != 0) {
		cin >> letter;

		bool result = false;
		// Check if string contains the character or not
		for (auto& elem : usedLetters)
		{
			if (elem == letter)
			{
				result = true;
				cout << "Letter " << letter << " has already been used\n";
				break;
			}
		}
		bool isInPassword = false;
		if (result == false) {
			for (auto& elem : password)
			{
				if (elem == letter)
				{
					isInPassword = true;
					goodLetters = goodLetters + letter;
				}
			}
			if (isInPassword == true) {
				for (auto& elemp : password)
				{
					if (isspace(elemp)) {
						cout << "  ";
					}
					else {
						bool res = false;
						for (auto& elemg : goodLetters)
						{
							if (elemg == elemp) {
								cout << elemp << " ";
								res = true;
								break;
							}
						}
						if (res == false) {
							cout << "_ ";
						}
					}
				}
			}
			else {
				usedLetters = usedLetters + letter;
				chances--;
			}
		}
		Sleep(1000);
		system("cls");
		drawHangman(chances);
		cout << "\nkategoria: " << kategoria;
		cout << endl;
		for (auto& elemp : password)
		{
			if (isspace(elemp)) {
				cout << "  ";
			}
			else {
				bool res = false;
				for (auto& elemg : goodLetters)
				{
					if (elemg == elemp) {
						cout << elemp << " ";
						res = true;
						break;
					}
				}
				if (res == false) {
					cout << "_ ";
				}
			}
		}
		cout << "\nUsed letters: ";
		for (auto& elem : usedLetters) {
			cout << elem << ", ";
		}
		cout << "\n";

		int guessedLettersCount = 0;
		int spaceCount = 0;
		for (auto& elemp : password)
		{
			if (isspace(elemp)) {
				spaceCount++;
			}
			else {
				for (auto& elemg : goodLetters)
				{
					if (elemg == elemp) {
						guessedLettersCount++;
						break;
					}
				}
				if (guessedLettersCount == password.length() - spaceCount) {
					cout << "You won\nGoing to main menu\n";
					chances = 0;
					win = true;
					Sleep(3000);
					system("cls");
				}
			}
		}
	}
	if (win == false) {
		cout << "You lost.\n The password was: " << password << "\nGoing to main menu";
		Sleep(5000);
		system("cls");
	}
}

void validate()
{
	char p;
	cout << "Choose which player is giving the keyword\n";
	cin >> p;
	if ((p >= 'a' && p <= 'z') || (p >= 'A' && p <= 'Z')) {
		cout << endl << p << " is not an integer\n";
		validate();
	}
	else {
		string password;
		switch (p) {
		case '1':
			cout << "Keyword from player 1:\n";
			cin.ignore();
			getline(cin, password); //to use this function you need to add -> #include <string>
			system("cls");
			mainGame2(password, p);
			break;
		case '2':
			cout << "Keyword from player 2:\n";
			cin.ignore();
			getline(cin, password);
			system("cls");
			mainGame2(password, p);
			break;
		default:
			cout << "Insert '1' or '2'\n";
			validate();
			break;
		}
	}
}

void twoPlayers()
{
	string p1Name, p2Name;
	cout << "Player 1 name: ";
	cin >> p1Name;
	cout << "Player 2 name: ";
	cin >> p2Name;
	system("cls");
	validate();
}

void singlePlayer()
{
	//tab[y][x] y=ilosc rzedow, x=ilosc kolumn

	cout << "Hasla sa bez polskich znakow\n";

	string kategoria;
	string keywords[8][10] = {
							{"siatkowka", "pilka nozna", "kregle", "narciarstwo", "saneczkarstwo", "rzut dyskiem", "rzut oszczepem", "koszykowka", "snowboard", "golf"},//sport dyscyplina
							{"wiedzmin 3 dziki gon", "dishonored", "undertale", "the legend of zelda", "prince of persia", "call of duty black ops cold war", "battlefield hardline", "far cry", "grand theft auto san andreas", "assassins creed"},//gra komputerowa
							{"na skraju jutra", "avatar istota wody", "pakt z morderca", "bodyguard zawodowiec", "wyscig smierci", "wiezien labiryntu", "duze dzieci", "teksanska masakra pila mechaniczna", "szybcy i wsciekli", "wiek adeline"},//film
							{"koloseum", "palac kultury", "louvre", "wieza eiffla"},//budowla
							{"berlin", "paryz", "wenecja", "warszawa", "bangkok", "las vegas", "tokio", "londyn", "braniewo", "rzym"},//miasto
							{"polak madry po szkodzie", "kto pod kim dolki kopie ten sam w nie wpada", "bez pracy nie ma kolaczy", "baba z wozu konu lzej", "biednemu zawsze wiatr w oczy", "bogatemu to i byk sie ocieli", "byc pracowitym jak pszczola", "co cie nie zabije, to cie wzmocni", "cel uswieca srodki", "co dwie glowy to nie jedna"},//powiedzenie, przyslowie
							{"pies", "kot", "swinka morska", "hipopotam", "papuga", "gepard", "hiena", "pantera", "nosorozec", "koala"},//zwierze
							{"polska", "stany zjednoczone", "indie", "wielka brytania", "ukraina", "chiny", "hiszpania", "niemcy", "francja", "argentyna"}//kraj
	};

	srand(time(NULL));
	int y;
	int x;
	y = rand() % 8;
	switch (y) {
		case 0:
			x = rand() % 10;
			kategoria = "sport dyscyplina";
			break;
		case 1:
			x = rand() % 10;
			kategoria = "gra komputerowa";
			break;
		case 2:
			x = rand() % 10;
			kategoria = "film";
			break;
		case 3:
			x = rand() % 4;
			kategoria = "budowla";
			break;
		case 4:
			x = rand() % 10;
			kategoria = "miasto";
			break;
		case 5:
			x = rand() % 10;
			kategoria = "powiedzenie, przyslowie";
			break;
		case 6:
			x = rand() % 10;
			kategoria = "zwierze";
			break;
		case 7:
			x = rand() % 10;
			kategoria = "kraj";
			break;
	}
	string password = keywords[y][x];
	mainGame(password, kategoria);
}

int main()
{
	bool isLoop = true;
	while (isLoop == true)
	{
		cout << "Choose game mode\nType '1' for one player\nType '2' for two players\n\nType 'quit' to exit the game\n\n";
		string choice;
		cin >> choice;
		if (choice == "1") {
			cout << "Single player mode selected\n";
			singlePlayer();
			//cout << ":)";
		}
		else if (choice == "2") {
			cout << "Two players mode selected\n";
			twoPlayers();
			//cout << ":)";
		}
		else if (choice == "quit") {
			cout << "Goodbye\n";
			system("pause");
			exit(0);
		}
		else {
			cout << "I don't understand. Try again\n";
			Sleep(5000);
			system("cls");
		}
	}
}