import { api } from "../api";

export default {
    namespaced: true,

    state: {
        tags: [],
        tagsForObject: []
    },

    actions: {
        getTags: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('tags/tags/',{params: params}).then((response) => {
                    state.commit('UPDATE_TAGS', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        },
        getTagsForObject: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('tags/tags_for_obj/',{params: params}).then((response) => {
                    state.commit('UPDATE_TAGS_FOR_OBJECT', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        }
    },

    mutations: {
        UPDATE_TAGS: (state, payload) => {
            state.tags = payload;
        },
        UPDATE_TAGS_FOR_OBJECT: (state, payload) => {
            state.tagsForObject = payload;
        },
        APPEND_TAGS: (state, payload) => {
            state.tagsForObject.push(...payload)
        }
    },

    getters: {
        tags: (state) => state.tags,
        tagsForObject: (state) => state.tagsForObject
    },
};