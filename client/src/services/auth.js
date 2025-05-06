import axios from 'axios';

const DOMAIN = process.env.REACT_APP_AUTH0_DOMAIN; // = 'dev-nzeet…auth0.com'
const CLIENT_ID = process.env.REACT_APP_AUTH0_CLIENT_ID;

export function sendAuthCode(email) {
  return axios.post(
    `https://${DOMAIN}/passwordless/start`,
    { client_id: CLIENT_ID, connection: 'email', send: 'code', email }
  );
}

export const verifyAuthCode = (email, code) => {
  return axios.post(
    'https://dev-nzeet1cd8b6nxgvb.us.auth0.com/oauth/token',
    {
      grant_type: 'http://auth0.com/oauth/grant-type/passwordless/otp',
      client_id: 'f9dQtAyZrRarx42RkY1snEZDWMSMzrvj',
      client_secret: 'T3dmS_ypsh44WnUAIy9rODbFMjw4N1ybAM2fAxrsM3Cpai4kDTWdSg3INzkGMElR', // Якщо потрібно
      email: email,
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

