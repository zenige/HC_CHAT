<template>
  <div class="vlearn-profile-menu vlearn-profile-menu-container">
    <div class="vlearn-profile-menu-header">
      <a href="#">
        <img class="profile-image" :src="defaultProfileUrl" />
      </a>
      <!-- <div class="profile-name">{{ (user && user.firstname) || '-' }} {{ (user && user.lastname) || '-' }}</div> -->
      <div class="profile-name">
        <!-- <template v-if="user && user.firstname">
          {{ user && user.firstname }} {{ user && user.lastname }}
        </template> -->
        <template>
          <a href="#"> <span>Login</span> </a>
          <span
            style="
              margin-left: 5px;
              margin-right: 5px;
              hover: {
                color: '#000000';
              }
            "
          >
            &nbsp;|&nbsp;</span
          >
          <a href="#">
            <span>Register</span>
          </a>
        </template>
      </div>
      <!-- <div class="profile-email">{{ user && user.email }}</div> -->
      <!-- <button class="red-hover-btn" @click="logout()">
        Sign out
      </button> -->
    </div>
    <!-- <div class="vlearn-profile-menu-body">
      <div>
        <template v-if="user && user.firstname && user && user.lastname">
          <nuxt-link :to="localePath('/profile')" class="vlearn-profile-menu-item">
            <div>Profile</div>
          </nuxt-link>
        </template>
        <div class="vlearn-profile-menu-item" @click="openChooseLanguageModal">
          <div>Language</div>
          <div class="txt_vl_20p_gray88_h_red language-selector">{{ currentLanguage }}</div>
        </div>
      </div>
    </div> -->

    <!-- <template v-if="workspaces.length > 0 && !superAdminUser">
      <div class="dropdown-item txt_vl_head d-flex flex-row text-left txt_black_nolink">
        <div class="w_150p txt_true_Reg">Workspace</div>
      </div>
      <nuxt-link
        v-for="workspace in workspaces"
        :key="workspace.id"
        :to="/workspace/ + workspace.id"
        class="dropdown-item txt_vl_head d-flex flex-row text-left"
      >
        <div class="w_150p">
          <img
            :src="(workspace.image && workspace.image.url) || defaultWorkspaceUrl"
            class="rounded-circle align-middle w-32p img-item"
            loading="lazy"
          />
          {{ workspace.name }}
        </div>
      </nuxt-link>
    </template> -->

    <!-- <div class="vlearn-profile-menu-footer">
      <div class="vlearn-profile-menu-link">
        <a href>Terms and Conditions</a>
      </div>
    </div> -->
    <!-- <v-learn-choose-language-modal :open="isShowingChooseLanguageModal" :onSelected="closeChooseLanguageModal" /> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import defaultProfileUrl from '~/assets/hc-libs/images/main/face_default.png'
// import defaultWorkspaceUrl from '~/assets/vlearn-libs/images/vlstore/default_photo_2.jpg'
// import { isSuperAdminUser } from '~/helpers/user'

export default {
  name: 'VlearnProfileMenu',
  data: () => ({
    // superAdminUser: false,
    // isShowingChooseLanguageModal: false,
    defaultProfileUrl,
    // defaultWorkspaceUrl,
  }),
  computed: {
    // ...mapState('auth', ['user']),
    // ...mapState('workspace', ['workspaces']),
    // currentLanguage() {
    //   return this.$i18n.locales.find(({ code }) => code === this.$i18n.locale).name
    // },
  },
  watch: {
    // user() {
    //   this.setSuperAdminUser()
    // },
  },
  created() {
    // this.setSuperAdminUser()
  },
  methods: {
    async logout() {
      // try {
      //   await this.$auth.logout()
      //   await this.$router.replace('/login')
      // } catch (error) {
      // } finally {
      //   // force page rerender when logged out
      //   setTimeout(() => {
      //     window.location.reload()
      //   }, 100)
      // }
      console.log('logged out')
    },
    // setSuperAdminUser() {
    //   this.superAdminUser = isSuperAdminUser(this.user || {})
    // },
    // openChooseLanguageModal() {
    //   this.isShowingChooseLanguageModal = true
    // },
    // closeChooseLanguageModal() {
    //   this.isShowingChooseLanguageModal = false
    // },
  },
}
</script>

<style lang="scss">
.vlearn-profile-menu {
  .vlearn-profile-menu-header {
    .profile-image {
      cursor: pointer;
      border: 1px solid #f2f2f2;
    }
    .profile-image:hover {
      opacity: 0.7;
    }
  }
  .language-selector {
    font-weight: normal;
  }

  &-container {
    user-select: none;
    position: absolute;
    cursor: auto;
    width: 300px;
    height: auto;
    box-shadow: 0 0rem 0.5rem rgba(0, 0, 0, 0.2);
    font-size: 1rem;
    border-radius: 0.4rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    right: 54px;
    color: #888888;
    background: #fff;
    top: 54px;
    z-index: 1;
  }

  &-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 16px;

    .profile {
      &-image {
        display: flex;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin: 20px 0;
        object-fit: cover;
      }

      &-name {
        display: flex;
        font-style: normal;
        font-weight: 600;
        color: #333;
        line-height: 1em;
        font-size: 20px;
      }

      &-email {
        display: flex;
        font-style: normal;
        color: #888;
        line-height: 1.35em;
        font-size: 16px;
        margin-bottom: 16px;
      }
    }
  }

  &-body {
    border-top: 1px solid #dddddd;
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  &-item {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 8px 16px;
    font-size: 20px;
    color: #333;
    line-height: 20px;
    flex-direction: column;
    font-weight: 600;
    width: auto;
    cursor: pointer;
    border-bottom: 1px solid #dddddd;

    &:hover {
      color: var(--vlearn-primary);
      background: #f5f5f5;
      transition: all 0.2s ease-in-out;
    }
  }

  &-footer {
    display: flex;
    padding: 10px 0 18px 0;
  }

  &-link {
    font-size: 18px;

    & a {
      color: #888;
    }

    &:hover {
      color: #888;
    }
  }

  .txt_vl_head {
    font-family: 'TrueTextBOnline-bold';
    font-style: normal;
    color: #000000;
    line-height: 1em;
    font-size: 20px;
  }

  .dropdown-item {
    display: flex;
    align-items: center;
    position: relative;
    outline: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    cursor: pointer;
    margin-bottom: 0;
    background: transparent;
    transition: background-color ease-in-out 0.15s, color ease-in-out 0.15s;

    &.txt_black_nolink {
      color: #000000 !important;
      background-color: transparent !important;
      cursor: default !important;
      font-weight: normal;
    }

    &:hover {
      text-decoration: none;
      background-color: #f5f5f5;
      color: #cc338b;
    }
  }

  .img-item {
    display: inline-block;
    width: 35px;
    height: 35px;
    object-fit: cover;
  }
  .vlearn-profile-menu-footer {
    .vlearn-profile-menu-link a:hover {
      color: #cc338b;
    }
  }
}

// @TODO: consider to move it in side component class without breaking other modules.
.red-hover-btn {
  width: auto;
  padding: 2.2px 20px;
  height: 34px;
  border: 1px solid #d9d9d9;
  border-radius: 5rem;
  font-size: 20px;
  background: #fff;
  color: #888;
  outline: 0 !important;

  &:hover {
    background: #cc338b;
    color: #fff;
    transition: all 0.3s ease-in-out;
  }
}
</style>
