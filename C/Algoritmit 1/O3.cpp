#include <iostream>
using namespace std;

class Node {
    public:
        char key;
        Node* left;
        Node* right;

        Node(char x, Node* left, Node* right){
            key = x;
            this->left = left;
            this->right = right;
        }
};

void preOrder(Node* root){
    cout << root->key;
    if (root->left != nullptr){
        preOrder(root->left);
    }
    if (root->right != nullptr){
        preOrder(root->right);
    }
}

void inOrder(Node* root){
    if (root->left != nullptr){
        inOrder(root->left);
    }
    cout << root->key;
    if (root->right != nullptr){
        inOrder(root->right);
    }
}

void postOrder(Node* root){
    if (root->left != nullptr){
        postOrder(root->left);
    }
    if (root->right != nullptr){
        postOrder(root->right);
    }
    cout << root->key;
}

int main() {

    /*          H
          D           L
        B   F       J   N
       A C E G     I K M O
     */

    Node* A = new Node('A', nullptr, nullptr);
    Node* C = new Node('C', nullptr, nullptr);
    Node* B = new Node('B', A, C);
    Node* E = new Node('E', nullptr, nullptr);
    Node* G = new Node('G', nullptr, nullptr);
    Node* F = new Node('F', E, G);
    Node* D = new Node('D', B, F);

    Node* I = new Node('I', nullptr, nullptr);
    Node* K = new Node('K', nullptr, nullptr);
    Node* J = new Node('J', I, K);
    Node* M = new Node('M', nullptr, nullptr);
    Node* O = new Node('O', nullptr, nullptr);
    Node* N = new Node('N', M, O);
    Node* L = new Node('L', J, N);

    Node* root = new Node('H', D, L);


    preOrder(root);
    cout << "\n";
    inOrder(root);
    cout << "\n";
    postOrder(root);
    if (0 == 1<1) {
        cout << "\n1<1 produces false which is 0";
    }
    return 0;
}
