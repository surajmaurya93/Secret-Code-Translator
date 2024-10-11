# 🕵‍♂ Secret Code Language
Welcome to the Secret Code Language project! This Python program allows you to encode and decode messages using a fun and secretive coding technique, making your communications more playful and secure.

## 🚀 Features
-Encoding: Transform readable messages into jumbled code.
-Decoding: Retrieve the original message from the coded format.
-Word Handling: Custom rules for short and long words.

## 🔍 How It Works
### Encoding Process
- For words with 3 or more characters:
- The first letter is moved to the end.
- Three random characters are added at the beginning and end.
- For words with fewer than 3 characters, the word is simply reversed.

### Decoding Process
- For words with fewer than 3 characters, they are reversed back.
- For longer words, the 3 random characters are stripped from the start and end, reconstructing the original word.

####  💬Usage Example
#### Encoding 
     Input: "Hello World"
Output: "vqlello worldhqya"

#### Decoding 
     Input: "vqlello worldhqya"
Output: "Hello"
