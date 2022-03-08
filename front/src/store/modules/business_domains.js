import { api } from "../api";

export default {
    namespaced: true,

    state: {
        domains: {},
    },

    actions: {
        getDomains: (state, params) => {
            // const response = await api.get("business_domains");
            // await commit("UPDATE_DOMAINS", response.data);
            return new Promise((resolve, reject) => {
                api.get('domains', {params: params}).then((response) => {
                    state.commit('UPDATE_DOMAINS', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })

        },
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