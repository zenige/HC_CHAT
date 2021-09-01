<template>
  <div class="authentication-layout">
    <div class="body">
      <Header :isDrawer="drawer" @onToggleDrawer="onSetDrawer()" />
      <div
        class="content-wrapper mx-auto overflow-hidden"
        style="margin-top: 52px"
      >
        <div class="content p-0">
          <Nuxt />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '~/components/headers/default.vue'
import Sidebar from '~/components/sidebars/default.vue'
import SidebarMain from '~/components/sidebars/main.vue'
// import { isSuperAdminUser } from '@/helpers/user'
// import { mapState } from 'vuex'

export default {
  components: {
    Header,
    Sidebar,
    SidebarMain,
  },
  async fetch() {
    // const { user } = this.$auth
    // const { workspaceId } = this.$route.params
    // if (user) {
    //   if (isSuperAdminUser(user)) {
    //     if (workspaceId) {
    //       await this.$store.dispatch('workspace/fetchWorkspace', { workspaceId })
    //     }
    //   } else {
    //     await this.$store.dispatch('workspace/fetchMyWorkspaces')
    //     if (workspaceId) {
    //       await this.$store.dispatch('workspace/fetchMyWorkspace', { workspaceId })
    //       await this.$store.dispatch('master/fetchClassLevels')
    //     }
    //   }
    // }
  },

  data: () => {
    return {
      drawer: false,
      isLogin: false,
    }
  },
  // computed: mapState('workspace', ['workspace']),
  // middleware: 'isAuthenticated',
  methods: {
    onSetDrawer() {
      this.drawer = !this.drawer
    },
    setHideDrawer(event) {
      this.drawer = false
    },
  },
}
</script>

<style lang="scss" scoped>
.authentication-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>
