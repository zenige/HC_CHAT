<template>
  <div>
    <div class="container mx-auto">
      <div class="row py-md-5">
        <div class="col-12 py-5 text-center">
          <span>
            <div class="row justify-content-center login-page">
              <LoginForm
                class="login-form"
                :title="$t('login.title')"
                :showInvalid="showInvalid"
                :values="values"
                :errors="errors"
              >
                <div class="separator"></div>
                <div class="accessory">
                  <NuxtLink
                    :to="localePath('/forgot-password')"
                    class="accessory__cta"
                    >{{ $t('login.forgotPassword') }}</NuxtLink
                  >
                  <div class="accessory-separator">|</div>
                  <NuxtLink
                    :to="localePath('/authentication/Register')"
                    class="accessory__cta"
                    >{{ $t('login.register') }}</NuxtLink
                  >
                </div>
              </LoginForm>
            </div>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { isSuperAdminUser } from '@/helpers/user'
// import { ADMIN_PANEL_ROUTE } from '@/routes.config'
// import { mapState } from 'vuex'
// import { ERROR_CODES } from '~/constants/statusCode'

// const BASE_URL = process.env.NUXT_ENV_API_ENDPOINT

export default {
  layout: 'noHeaderLayout',
  components: {
    LoginForm: () => import('~/components/authentication/loginForm.vue'),
  },
  data() {
    return {
      // token: '',
      // isShowingChooseLanguageModal: false,
      // BASE_URL,
      // version: process.env.NUXT_ENV_VERSION,
      showInvalid: false,
      values: {
        email: '',
        password: '',
      },
      errors: {
        email: '',
        password: '',
      },
    }
  },
  computed: {
    // ...mapState('auth', ['user']),
    // ...mapState('workspace', ['workspaces']),
    // currentLanguage() {
    //   return this.$i18n.locales.find(({ code }) => code === this.$i18n.locale).name
    // },
  },

  methods: {
    // async handleSubmit({ email, password }) {
    //   await this.$auth
    //     .loginWith('local', {
    //       data: { email, password },
    //     })
    //     .catch((error) => {
    //       if (!error.response) {
    //         return
    //       }
    //       const { data } = error.response
    //       if (data && data.error.code === ERROR_CODES.EMAIL_NOT_VERIFIED) {
    //         this.$router.push({ path: this.localePath('/confirmation'), query: { email } })
    //       } else {
    //         this.showInvalid = true
    //       }
    //     })
    //   if (!this.$auth.user) {
    //     return
    //   }
    //   if (isSuperAdminUser(this.$auth.user)) {
    //     await this.$router.push(this.localePath(ADMIN_PANEL_ROUTE.path))
    //   } else {
    //     await this.$router.push(this.localePath('/workspace/join'))
    //   }
    // },
    // openChooseLanguageModal() {
    //   this.isShowingChooseLanguageModal = true
    // },
  },
}
</script>

<style lang="scss">
// @TODO: find the other way to resolve scss path
@import '~assets/scss/layouts.scss';

@media (min-width: 576px) {
  .container,
  .container-sm {
    max-width: 540px;
  }
}
@media (min-width: 768px) {
  .container,
  .container-sm,
  .container-md {
    max-width: 720px; /*720*/
  }
  /* .fitscreen .col, .fitscreen .col-1, .fitscreen .col-10, .fitscreen .col-11, .fitscreen .col-12, .fitscreen .col-2, .fitscreen .col-3, .fitscreen .col-4, .fitscreen .col-5, .fitscreen .col-6, .fitscreen .col-7, .fitscreen .col-8, .fitscreen .col-9, .fitscreen .col-auto, .fitscreen .col-lg, .fitscreen .col-lg-1, .fitscreen .col-lg-10, .fitscreen .col-lg-11, .fitscreen .col-lg-12, .fitscreen .col-lg-2, .fitscreen .col-lg-3, .fitscreen .col-lg-4, .fitscreen .col-lg-5, .fitscreen .col-lg-6, .fitscreen .col-lg-7, .fitscreen .col-lg-8, .fitscreen .col-lg-9, .fitscreen .col-lg-auto, .fitscreen .col-md, .fitscreen .col-md-1, .fitscreen .col-md-10, .fitscreen .col-md-11, .fitscreen .col-md-12, .fitscreen .col-md-2, .fitscreen .col-md-3, .fitscreen .col-md-4, .fitscreen .col-md-5, .fitscreen .col-md-6, .fitscreen .col-md-7, .fitscreen .col-md-8, .fitscreen .col-md-9, .fitscreen .col-md-auto, .fitscreen .col-sm, .fitscreen .col-sm-1, .fitscreen .col-sm-10, .fitscreen .col-sm-11, .fitscreen .col-sm-12, .fitscreen .col-sm-2, .fitscreen .col-sm-3, .fitscreen .col-sm-4, .fitscreen .col-sm-5, .fitscreen .col-sm-6, .fitscreen .col-sm-7, .fitscreen .col-sm-8, .fitscreen .col-sm-9, .fitscreen .col-sm-auto, .fitscreen .col-xl, .fitscreen .col-xl-1, .fitscreen .col-xl-10, .fitscreen .col-xl-11, .fitscreen .col-xl-12, .fitscreen .col-xl-2, .fitscreen .col-xl-3, .fitscreen .col-xl-4, .fitscreen .col-xl-5, .fitscreen .col-xl-6, .fitscreen .col-xl-7, .fitscreen .col-xl-8, .fitscreen .col-xl-9, .fitscreen .col-xl-auto {
    position: relative;
    width: 100%;
    min-height: 1px;
    padding-right: .3rem;
    padding-left: .3rem;
  } */
}
@media (min-width: 992px) {
  .container,
  .container-sm,
  .container-md,
  .container-lg {
    max-width: 960px;
  }
}
@media (min-width: 1200px) {
  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl {
    max-width: 1200px;
  }
  .container-lg-plus {
    max-width: 1160px;
  }
  .container_short {
    max-width: 900px;
  }
}

.login-page {
  a {
    color: #999999;
  }

  // .login-form {
  //   position: relative;
  //   top: -40px;
  // }

  .btn {
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .separator {
    margin: 24px 0;
  }

  .accessory {
    display: grid;
    align-items: center;
    grid-auto-flow: column;
    max-width: 180px;
    margin: 0 auto;
    column-gap: 4px;
    font-size: 18px;
    color: var(--healthcare-grey-dark);

    &-separator {
      color: var(--healthcare-grey-dark);
    }

    &__cta:hover {
      color: var(--healthcare-primary);
    }
  }
}

.txt_grey_99 {
  font-size: 18px;
}
</style>
