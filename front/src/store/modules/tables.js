import { api } from "../api";

export default {
    namespaced: true,

    state: {
        tables: [],
        tableHierarchy: []
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
        getTableHierarchy: (state, params) => {
            return new Promise((resolve, reject) => {
                api.get('table_hierarchy/', {params: params}).then((response) => {
                    state.commit('UPDATE_TABLE_HIERARCHY', response.data);
                    resolve(response.data);
                }).catch((error) => {
                    reject(error);
                })
            })
        }
    },

    mutations: {
        UPDATE_TABLES: (state, payload) => {
            state.tables = payload;
        },
        UPDATE_TABLE_HIERARCHY: (state, payload) => {
            state.tableHierarchy = payload;
        },
    },

    getters: {
        tables: (state) => {
            return state.tables
        },
        tableHierarchy: (state) => {
            return state.tableHierarchy
        }
    },
};