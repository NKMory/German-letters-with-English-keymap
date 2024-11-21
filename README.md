# German-letters-with-English-keymap
 With this script you won't need German keymap anymore!

### How It Works

- **Vowels to vowels with umlauts**: Typing two dots after a vowel (e.g., `a..`, `A..`) will replace it with the corresponding umlauted character (e.g., `ä`, `Ä`).
- **`sss` and `SSS` to `ß`**: Typing `sss` or `SSS` will be replaced with the German character `ß`.
- It only triggers the replacement if the letters and dots are typed consecutively. For example, typing `a.,.` (with a comma between the dots) will not trigger the replacement.

### Example

- Typing `a..` will automatically convert it to `ä`.
- Typing `sss` will automatically convert it to `ß`.

### Installation and Usage

1. **Install pynput**
2. **Run the script**: The script will listen to your keyboard input globally.
3. **Start typing**: Use `a..` for `ä`, `A..` for `Ä`, and `sss` for `ß`.

### Notes

- Ensure that you type the character combinations correctly without extra letters or punctuation for the replacements to trigger.
- You can cancel a replacement by typing any character other than a dot and erasing it before continuing.
