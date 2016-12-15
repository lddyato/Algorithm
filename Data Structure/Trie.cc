// Trie implements the data structure trie.
// Read more: https://en.wikipedia.org/wiki/Trie

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// TrieNode represents the nodes in trie.
struct TrieNode {
    bool isWord;
    std::unordered_map<char, TrieNode*> children;

    ~TrieNode() {
        for (auto iter = children.begin(); iter != children.end(); ++iter) {
            delete iter->second;
        }
    }
};

// Trie implements trie.
class Trie {
public:
    Trie(): root(new TrieNode()) {}

    ~Trie() {
        delete root;
    }

    // insert inserts a word to the trie.
    void insert(std::string word) {
        TrieNode* child;

        auto node = root;
        for (auto ch: word) {
            child = node->children[ch];
            if (child == nullptr) {
                child = new TrieNode();
            }
            node = (node->children[ch] = child);
        }
        node->isWord = true;
    }

    // search finds out whether a word is in the trie.
    bool search(std::string word) {
        auto node = root;
        for (auto ch: word) {
            node = node->children[ch];
            if (node == nullptr) {
                return false;
            }
        }
        return node->isWord;
    }

private:
    TrieNode* root;
};

int main() {
    auto trie = std::unique_ptr<Trie>(new Trie());

    auto words = std::vector<std::string>{
        "romane", "romanus", "romulus", "rubens",
        "ruber", "rubicon", "rubicundus"
    };

    for (auto iter = words.begin(); iter != words.end(); ++iter) {
        trie->insert(*iter);
    }

    for (auto iter = words.begin(); iter != words.end(); ++iter) {
        std::cout << trie->search(*iter) << std::endl;
    }

    std::cout << trie->search("not exist") << std::endl;
}
