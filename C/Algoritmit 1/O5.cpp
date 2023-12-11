#include <iostream>
#include <string>
#include <vector>
using namespace std;

string reverseString(string s){
    vector<string> words;
    string reversedString;
    string word = "";
    for(int i = 0; i < int(s.length()); i++){
        if(s[i] == ' ' && s[i+1] != ' '){
            words.push_back(word);
            word = "";
            continue;
        }
        if (s[i] != ' '){
            word += s[i];
        }
    }
    words.push_back(word);
    for(int i = words.size(); i > 0; i--){
        reversedString += words.at(i-1);
        reversedString += " ";
    }
    return reversedString;
}


int main() {
    string sentence = "     algoritmien opiskelu on      kivaa     ";
    cout << "\n" << reverseString(sentence);
    return 0;
}