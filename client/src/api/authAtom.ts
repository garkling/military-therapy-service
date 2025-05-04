// authAtom.ts
import { atom } from 'jotai';

type AuthAtom = {
    accessToken: string | null;
    idToken: string | null;
    status: 'loading' | 'fulfilled'
}

export const authAtom = atom<AuthAtom>({
    accessToken: null,
    idToken: null,
    status: 'loading'
})
