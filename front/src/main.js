import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";

import 'gitart-vue-dialog/dist/style.css'
import { GDialog } from 'gitart-vue-dialog'

const app = createApp(App);
app.component('GDialog', GDialog);
app.use(store);
app.mount("#app");