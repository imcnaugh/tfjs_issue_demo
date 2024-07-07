import * as tf from '@tensorflow/tfjs';
import express from 'express';

const app = express();

// expose the tfjs-model folder as static files
app.use(express.static('tfjs-model'));

app.get('/predict', async (req, res) => {
    const model = await tf.loadLayersModel('http://localhost:3000/model.json');
    const tensor = tf.tensor2d([[0]])
    const prediction = model.predict(tensor).arraySync();
    res.send(prediction);
})

app.listen(3000, () => {
    console.log('Server running on port 3000');
});