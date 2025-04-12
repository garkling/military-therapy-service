import React, { Component } from 'react';
import axios from 'axios';
import Pusher from 'pusher-js';
import ChatList from './components/ChatList';
import ChatBox from './components/ChatBox';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: '',
      username: '',
      chats: [],
      users: []
    };
  }

  componentDidMount() {
    axios.get('http://localhost:5000/getUser')
      .then(response => {
        this.setState({ username: response.data.username });
      })
      .catch(error => {
        console.error('Error fetching username:', error);
        this.setState({ username: 'Anonymous' });
      });

    axios.get('http://localhost:5000/getUsers')
      .then(response => {
        this.setState({ users: response.data.users });
      })
      .catch(error => {
        console.error('Error fetching users:', error);
      });

    const pusher = new Pusher('6b0a4557a760df1f15c3', {
      cluster: 'eu',
      encrypted: true
    });

    const channel = pusher.subscribe('chat');
    channel.bind('message', data => {
      this.setState(prevState => ({
        chats: [...prevState.chats, data]
      }));
    });

    this.handleTextChange = this.handleTextChange.bind(this);
    this.handleSendMessage = this.handleSendMessage.bind(this);
  }


  handleTextChange(e) {
    if (e.keyCode === 13) {
        this.handleSendMessage();
    } else {
        this.setState({ text: e.target.value });
    }
}

async handleSendMessage() {
    const { username, text } = this.state;

    if (!text.trim()) return;

    const payload = { username, message: text };

    try {
        await axios.post('http://localhost:5000/message', payload);
        this.setState({ text: '' });
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

  render() {
    return (
      <div className="App">
        <section>
          <ChatList
            chats={this.state.chats}
            users={this.state.users}
            currentUsername={this.state.username}
            handleSendMessage={this.handleSendMessage}
          />
          <ChatBox
            text={this.state.text}
            handleTextChange={this.handleTextChange}
            handleSendMessage={this.handleSendMessage}
          />
        </section>
      </div>
    );
  }
}

export default App;
