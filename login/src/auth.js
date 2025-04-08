// auth.js
import { createAuth0Client } from "@auth0/auth0-spa-js";

const auth0Promise = createAuth0Client({
  domain: "dev-nzeet1cd8b6nxgvb.us.auth0.com", // наприклад, dev-xxxxx.us.auth0.com
  client_id: "XbLqULjdINkfSp6Wxj4a7K0RiZJxqTrC",
});

export default auth0Promise;
