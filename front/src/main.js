import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";

import 'gitart-vue-dialog/dist/style.css'
import { GDialog } from 'gitart-vue-dialog'
import VNetworkGraph from "v-network-graph"
import "v-network-graph/lib/style.css"
import loader from "vue-ui-preloader";
import router from './router'

const app = createApp(App).use(router);
app.component('GDialog', GDialog);
app.use(VNetworkGraph);
app.use(loader);
app.use(store);
app.mount("#app");