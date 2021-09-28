<template>
  <div class="sidebar-main-container">
    <NuxtLink :to="localePath('/')" class="sidebar-menu-logo">
      <img
        src="~/assets/hc-libs/images/main/logo_healthcare2.png"
        alt="healthcare-logo"
        class="sidebar-menu-logo-img"
      />
    </NuxtLink>
    <NuxtLink :to="localePath('/user/profile')" class="sidebar-menu-profile">
      <img
        class="sidebar-menu-profile-img"
        src="~/assets/hc-libs/images/main/face_default.png"
        alt="user-profile"
      />
      <div class="sidebar-menu-profile-item">
        <div class="sidebar-menu-profile-item-name">Bawornsak Luachan</div>
        <div class="sidebar-menu-profile-item-email">nuiwitclup@gmail.com</div>
      </div>
    </NuxtLink>
    <div class="sidebar-menu-main-disabled">
      <i class="mi-chat-bubble sidebar-menu-main-icon"></i>
      <span>Chatbot Training</span>
    </div>
    <div class="collapse-chatbot-sidebar">
      <div class="sidebar-menu-main-item" @click="linkTo('/')">New Word</div>
      <div
        class="sidebar-menu-main-item"
        @click="linkTo('/chatbot-training/trained-word')"
      >
        Trained Word
      </div>
      <div
        class="sidebar-menu-main-item"
        @click="linkTo('/chatbot-training/feature-management')"
      >
        Feature Management
      </div>
      <div
        class="sidebar-menu-main-item"
        @click="linkTo('/chatbot-training/group-management')"
      >
        Group Management
      </div>
    </div>

    <NuxtLink
      :to="localePath('/dashboard/all-patient-group')"
      class="sidebar-menu-main"
    >
      <i class="mi-dashboard sidebar-menu-main-icon"></i>
      <span>Dashboard</span>
    </NuxtLink>

    <div class="sidebar-menu-main-signout">
      <NuxtLink :to="localePath('/login')">
        <img
          src="~assets/hc-libs/images/main/logout.svg"
          width="20"
          class="sidebar-menu-main-icon"
        />
        <span>Signout</span>
      </NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({}),
  computed: {},
  watch: {},
  beforeMount() {},
  methods: {
    linkTo(path) {
      this.$router.push(path)
    },
  },
}
</script>

<style lang="scss">
.sidebar-main-container {
  @media (max-width: 1200px) {
    display: none;
  }
  display: flex;
  position: fixed;
  flex-direction: column;
  border-right: 1px solid #ececec;
  width: 256px;
  background: #fff;
  border-bottom: 1px solid #dddddd;
  height: 100%;
  box-sizing: border-box;
  z-index: 998;
  box-shadow: 6px 0px 18px 0px rgba(0, 0, 0, 0.06);
}
.sidebar-menu {
  &-logo {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: auto;
    padding-top: 1rem;

    &-img {
      width: 166px;
      height: 42px;
    }
  }

  &-profile {
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto;
    flex-direction: row;
    max-width: 100%;
    font-family: 'Prompt-Medium';
    margin-top: 1rem;
    padding: 1rem;

    &-img {
      max-width: 46px;
      max-height: 46px;
      border-radius: 50%;
    }

    &-item {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      cursor: pointer;
      height: auto;
      padding-left: 1rem;
      &-name {
        font-family: 'Prompt-Medium';
        font-size: 14px;
        color: #192a3e;
      }
      &-email {
        font-family: 'Prompt-Medium';
        font-size: 11px;
        color: #90a0b7;
      }
    }

    &:hover {
      transition: all 0.2s ease-in-out;
      background-color: #f5f5f5;
      .sidebar-menu-profile-item-name {
        color: #10c4cc;
        transition: all 0.2s ease-in-out;
      }
    }
  }
  &-main {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    padding: 1.5rem 1rem 0.5rem 2rem;
    cursor: pointer;
    max-width: 100%;
    font-family: 'Prompt-Medium';
    font-size: 13px;
    color: #334d6e;
    text-align: left;
    &:hover {
      color: #10c4cc;
      transition: all 0.2s ease-in-out;
    }

    &-disabled {
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-items: center;
      padding: 1rem 1rem 0 2rem;
      max-width: 100%;
      span {
        font-family: 'Prompt-Medium';
        font-size: 13px;
        color: #334d6e;
        text-align: left;
      }
    }

    &-signout {
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-items: flex-end;
      height: 100%;
      a {
        font-family: 'Prompt-Medium';
        font-size: 13px;
        color: #334d6e;
        text-align: left;
        display: flex;
        align-items: center;
        width: 100%;
        padding: 0 1rem 2rem 2rem;
        &:hover {
          color: #10c4cc;
        }
      }
    }

    &-icon {
      color: #c2cfe0;
      margin-right: 1rem;
      font-size: 20px;
    }

    &-item {
      cursor: pointer;
      max-width: 100%;
      font-family: 'Prompt-Regular';
      font-size: 13px;
      color: #334d6e;
      padding: 1rem 1rem 0 5rem;
      max-width: 100%;
      &:hover {
        color: #10c4cc;
        transition: all 0.2s ease-in-out;
      }
    }
  }
}
</style>
