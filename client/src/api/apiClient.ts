// useApi.js
import { useAtomValue } from 'jotai';
import { authAtom } from './authAtom.ts';

const API_BASE_URL = 'http://localhost:8085/api/v1';

export const useApi = () => {
    const { accessToken } = useAtomValue(authAtom);

    const headers = {
        'Content-Type': 'application/json',
        ...(accessToken && { 'Authorization': `Bearer ${accessToken}` }),
    };

    const handleResponse = async (response) => {
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'API Error');
        }
        return response.json();
    };

    return {
        createChat: (participant_id) =>
            fetch(`${API_BASE_URL}/chats`, {
                method: 'POST',
                headers,
                body: JSON.stringify({ participant_id }),
            }).then(handleResponse),

        getChat: (chat_id) =>
            fetch(`${API_BASE_URL}/chats/${chat_id}`, {
                method: 'GET',
                headers,
            }).then(handleResponse),

        listChats: () =>
            fetch(`${API_BASE_URL}/chats`, {
                method: 'GET',
                headers,
            }).then(handleResponse),

        sendMessage: (chat_id, message) =>
            fetch(`${API_BASE_URL}/chats/${chat_id}/messages`, {
                method: 'POST',
                headers,
                body: JSON.stringify({ message }),
            }).then(handleResponse),

        listMessages: (chat_id) =>
            fetch(`${API_BASE_URL}/chats/${chat_id}/messages`, {
                method: 'GET',
                headers,
            }).then(handleResponse),
    };
};
