// RadixTree implements the data structure radix tree.
// Read more: https://en.wikipedia.org/wiki/Radix_tree

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

struct RadixTreeNode {
    std::string chunk;
    bool isWord;
    std::unordered_map<char, RadixTreeNode*> children;

    RadixTreeNode() = default;

    RadixTreeNode(std::string chunk, bool isWord):
        chunk(chunk), isWord(isWord) {}

    ~RadixTreeNode() {
        for (auto iter = children.begin(); iter != children.end(); ++iter) {
            delete iter->second;
        }
    }
};

using children_t = std::unordered_map<char, RadixTreeNode*>;

// RadixTree implements radix tree.
class RadixTree {
public:
    RadixTree(): root(new RadixTreeNode()) {}

    ~RadixTree() {
        delete root;
    }

    // insert inserts a word to the radix tree.
    void insert(std::string word) {
        int i = 0, n = word.size();
        auto node = root;

        while (i < n) {
            if (node->children[word[i]] == nullptr) {
                node->children[word[i]] = new RadixTreeNode(
                    word.substr(i), true
                );
                return;
            }
            node = node->children[word[i]];

            int j = 0, m = node->chunk.size();
            for (; i < n && j < m && word[i] == node->chunk[j]; ++i, ++j) {}

            // split
            if (j < m) {
                auto child = new RadixTreeNode(
                    node->chunk.substr(j),
                    node->isWord
                );
                child->children = node->children;

                node->chunk = node->chunk.substr(0, j);
                node->isWord = false;
                node->children = children_t{{child->chunk[0], child}};
            }
        }
        node->isWord = true;
    }

    // search finds out whether a word is in the radix tree.
    bool search(std::string word) {
        auto node = root;

        while (!word.empty()) {
            if (node->children[word[0]] == nullptr) {
                return false;
            }
            node = node->children[word[0]];

            if (word.size() < node->chunk.size() || (
                    word.size() > node->chunk.size() &&
                    word.substr(0, node->chunk.size()) != node->chunk)) {
                return false;
            }

            if (word.size() == node->chunk.size()) {
                return word == node->chunk && node->isWord;
            }

            word = word.substr(node->chunk.size());
        }

        return false;
    }

private:
    RadixTreeNode* root;
};

int main() {
    std::unique_ptr<RadixTree> radixTree(new RadixTree());

    auto words = std::vector<std::string>{
        "romane", "romanus", "romulus", "rubens",
        "ruber", "rubicon", "rubicundus"
    };

    for (auto iter = words.begin(); iter != words.end(); ++iter) {
        radixTree->insert(*iter);
    }

    for (auto iter = words.begin(); iter != words.end(); ++iter) {
        std::cout << radixTree->search(*iter) << std::endl;
    }

    std::cout << radixTree->search("not exist") << std::endl;
}
