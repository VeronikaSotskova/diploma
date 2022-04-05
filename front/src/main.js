import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";

import 'gitart-vue-dialog/dist/style.css'
import { GDialog } from 'gitart-vue-dialog'
import TreeView from "vue-json-tree-view"
import router from './router'

const app = createApp(App).use(router);
app.component('GDialog', GDialog);
app.use(TreeView);
app.use(store);
app.mount("#app");