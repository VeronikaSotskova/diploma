import {api} from "../api";

export default {
    namespaced: true,
    state: {
        entity: {},
        graph: {
            nodes: {},
            edges: {},
            currentNode: ''
        }
    },
    actions: {
        async getDependencies({commit}, params) {
            const response = await api.get('dbt/get_dependencies/', {params: params})
            await commit('UPDATE_GRAPH', response.data.graph)
            await commit('UPDATE_ENTITY', response.data.entity)
        },
        async addTags({commit}, params) {
            const response = await api.patch('tags/add_tags/', params)
            await commit('APPEND_TAGS', response.data)
        }
    },

    mutations: {
        UPDATE_GRAPH: (state, payload) => {
            state.graph = payload;
        },
        UPDATE_ENTITY: (state, payload) => {
            state.entity = payload;
        },
        APPEND_TAGS: (state, payload) => {
            state.entity.tags = payload
        }
    },

    getters: {
        nodes: state => state.graph.nodes,
        edges: state => state.graph.edges,
        currentNode: state => state.graph.current_node,
        tags: state => state.entity.tags,
        entity: state => state.entity
    },
};