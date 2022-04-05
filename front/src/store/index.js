import Vuex from "vuex";
import business_domains from "@/store/modules/business_domains";
import tables from "@/store/modules/tables";

export default new Vuex.Store({
    modules: {
        business_domains,
        tables
    },
});
