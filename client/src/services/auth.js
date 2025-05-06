import axios from 'axios';

const DOMAIN = process.env.REACT_APP_AUTH0_DOMAIN; // = 'dev-nzeet…auth0.com'
const CLIENT_ID = process.env.REACT_APP_AUTH0_CLIENT_ID;
const CLIENT_SECRET = process.env.REACT_APP_AUTH0_CLIENT_SECRET

export function sendAuthCode(email) {
  return axios.post(
    `https://${DOMAIN}/passwordless/start`,
    { client_id: CLIENT_ID, client_secret: CLIENT_SECRET, connection: 'email', send: 'code', email }
  );
}

export const verifyAuthCode = (email, code) => {
  return axios.post(
    `https://${DOMAIN}/oauth/token`,
    {
      grant_type: 'http://auth0.com/oauth/grant-type/passwordless/otp',
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET, // Якщо потрібно
      email: email,
      username: email,
      realm: "email",
      otp: code,
      scope: 'openid profile email',
    },
    {
      headers: {
        'Content-Type': 'application/json',
      },
    }
  );
};

