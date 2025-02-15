const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/recordData', (req, res) => {
    const { trial, correctAnswer, participantAnswer } = req.body;
    const data = `Trial ${trial}: Correct Answer: ${correctAnswer}, Participant Answer: ${participantAnswer}\n`;

    fs.appendFile('data.txt', data, (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error recording data.');
        } else {
            console.log(`Data recorded: ${data}`);
            res.status(200).send('Data recorded successfully.');
        }
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});