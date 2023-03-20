<script>
import svgComp from './SVG/svg-comp.vue';
export default {
  components: { svgComp },
  name: 'HelloWorld',
}
</script>

<template>
  <svg-comp :dataSource="'./comps/commits.json'"></svg-comp>
</template>

<style scoped>
.close-btn:hover {
  cursor: pointer;
}
</style>