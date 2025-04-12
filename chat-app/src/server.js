const express = require('express');
const bodyParser = require('body-parser');
const Pusher = require('pusher');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const pusher = new Pusher({
  appId: '1971472',
  key: '6b0a4557a760df1f15c3',
  cluster: 'eu',
  useTLS: true
});

app.post('/message', (req, res) => {
  const { username, message } = req.body;
  pusher.trigger('chat', 'message', { username, message });
  res.send({ success: true });
});

app.listen(4000, () => {
  console.log('Server is running on port 4000');
});
