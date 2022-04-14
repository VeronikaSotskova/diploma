import { api } from "../api";

export default {
    namespaced: true,

    state: {
        domains: {},
    },

    actions: {
        getDomains: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('domains/', {params: params}).then((response) => {
                    state.commit('UPDATE_DOMAINS', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        },
        changeColor: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('change_color/', {params: params}).then((response) => {
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        }
    },

    mutations: {
        UPDATE_DOMAINS: (state, payload) => {
            state.domains = payload;
        },
    },

    getters: {
        domains: (state) => {
            return state.domains
        },
    },
};