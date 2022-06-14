import { api } from "../api";

export default {
    namespaced: true,

    state: {
        hintObjects: [],
        searchObjects: {}
    },

    actions: {
        async getHintObjects({ commit }, params, cancelToken) {
            const response = await api.get('hint_objects/', {params: params, cancelToken})
            await commit('UPDATE_HINT_OBJECTS', response.data)
        },
        async getSearchObjects({ commit }, params) {
            const response = await api.get('search/', {params: params})
            await commit('UPDATE_SEARCH_OBJECTS', response.data)
        }
    },

    mutations: {
        UPDATE_HINT_OBJECTS: (state, payload) => {
            state.hintObjects = payload;
        },
        UPDATE_SEARCH_OBJECTS: (state, payload) => {
            state.searchObjects = payload;
        }
    },

    getters: {
        hintObjects: state => state.hintObjects,
        searchObjects: state => state.searchObjects
    },
};