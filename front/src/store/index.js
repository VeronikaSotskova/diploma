import Vuex from "vuex";
import business_domains from "@/store/modules/business_domains";
import search from "@/store/modules/search";
import tags from "@/store/modules/tags";
import dbt from "@/store/modules/dbt";


export default new Vuex.Store({
    modules: {
        business_domains,
        tags,
        search,
        dbt
    },
});
