import { api } from "../api";

export default {
    namespaced: true,

    state: {
        tables: [],
    },

    actions: {
        getTables: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('tables/', {params: params}).then((response) => {
                    state.commit('UPDATE_TABLES', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })

        },
    },

    mutations: {
        UPDATE_TABLES: (state, payload) => {
            state.tables = payload;
        },
    },

    getters: {
        tables: (state) => {
            return state.tables
        },
    },
};