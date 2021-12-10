<template>
  <div class="sidebar-main-hidden main-skin-layout">
    <div class="body">
      <div class="content-wrapper mx-auto overflow-hidden">
        <div class="content p-0 main-skin-content">
          <Nuxt />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},

  data: () => {
    return {}
  },
}
</script>

<style lang="scss">
.main-skin-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>
