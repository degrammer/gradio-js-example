const fs = require('fs')
const { reverseWords } = require('../reverseWords')

fs.writeFile('./out/reverse.js', reverseWords.toString(), (error) => {
    if (error) {
        console.error('Failed to save file')
        return
    }
    console.log('file saved!')
})