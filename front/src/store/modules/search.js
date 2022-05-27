import { api } from "../api";

export default {
    namespaced: true,

    state: {
        tableHierarchyConfig: {},
        tableHierarchyNodes: {},
        hintObjects: [],
        searchObjects: {}
    },

    actions: {
        getTableHierarchy: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('hint_objects/', {params: params}).then((response) => {
                    state.commit('UPDATE_TABLE_HIERARCHY_CONFIG', response.data.config);
                    state.commit('UPDATE_TABLE_HIERARCHY_NODES', response.data.nodes);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        },
        async getHintObjects({ commit }, params) {
            const response = await api.get('hint_objects/', {params: params})
            await commit('UPDATE_HINT_OBJECTS', response.data)
        },
        async getSearchObjects({ commit }, params) {
            const response = await api.get('search/', {params: params})
            await commit('UPDATE_SEARCH_OBJECTS', response.data)
        }
    },

    mutations: {
        UPDATE_TABLE_HIERARCHY_CONFIG: (state, payload) => {
            state.tableHierarchyConfig = payload;
        },
        UPDATE_TABLE_HIERARCHY_NODES: (state, payload) => {
            state.tableHierarchyNodes = payload;
        },
        UPDATE_HINT_OBJECTS: (state, payload) => {
            state.hintObjects = payload;
        },
        UPDATE_SEARCH_OBJECTS: (state, payload) => {
            state.searchObjects = payload;
        }
    },

    getters: {
        tableHierarchyConfig: state => state.tableHierarchyConfig,
        tableHierarchyNodes: state => state.tableHierarchyNodes,
        hintObjects: state => state.hintObjects,
        searchObjects: state => state.searchObjects
    },
};