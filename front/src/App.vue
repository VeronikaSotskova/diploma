<template lang="pug">
router-view
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@font-face {
  font-style: normal;
  font-weight: 400;
  font-family: "Montserrat";
  font-display: swap;
  src:
    url("assets/fonts/montserrat-regular.woff2") format("woff2"),
    url("assets/fonts/montserrat-regular.woff") format("woff");
}
@font-face {
  font-style: normal;
  font-weight: 500;
  font-family: "Montserrat";
  font-display: swap;
  src:
    url("assets/fonts/montserrat-medium.woff2") format("woff2"),
    url("assets/fonts/montserrat-medium.woff") format("woff");
}
@font-face {
  font-style: normal;
  font-weight: 600;
  font-family: "Montserrat";
  font-display: swap;
  src:
    url("assets/fonts/montserrat-semibold.woff2") format("woff2"),
    url("assets/fonts/montserrat-semibold.woff") format("woff");
}
@font-face {
  font-style: normal;
  font-weight: 700;
  font-family: "Montserrat";
  font-display: swap;
  src:
    url("assets/fonts/montserrat-bold.woff2") format("woff2"),
    url("assets/fonts/montserrat-bold.woff") format("woff");
}
#app {
  font-family: "Montserrat", "Arial", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.navbar {
  background-color: #e6e6fa
}
</style>