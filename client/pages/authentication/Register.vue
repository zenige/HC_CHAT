<template>
  <div>
    <div class="container mx-auto">
      <div class="row">
        <div class="col-12 py-5 text-center">
          <span>
            <div class="row justify-content-center">
              <RegisterForm @onSubmit="handleSubmit"></RegisterForm>
            </div>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { ERROR_CODES } from '~/constants/statusCode'

export default {
  layout: 'noHeaderLayout',
  components: {
    RegisterForm: () => import('~/components/authentication/registerForm.vue'),
  },
  data() {
    return {
      // isShowingChooseLanguageModal: false,
    }
  },
  computed: {
    // currentLanguage() {
    //   return this.$i18n.locales.find(({ code }) => code === this.$i18n.locale)
    //     .name
    // },
  },
  // middleware: 'isPortal',
  methods: {
    async handleSubmit(values) {
      // console.log('Register')
    },
    // openChooseLanguageModal() {
    //   this.isShowingChooseLanguageModal = true
    // },
  },
}
</script>

<style lang="scss">
@import '~assets/scss/layouts.scss';

// .container {
//   padding-left: 0.9375rem; /*15px = 0.9375rem*/
//   padding-right: 0.9375rem; /*15px = 0.9375rem*/
// }

// .register-page {
//   // .change-language-btn {
//   //   &:hover {
//   //     color: var(--healthcare-primary);
//   //   }
//   // }

//   a {
//     color: #999999;
//   }

//   // .login-form {
//   //   position: relative;
//   //   top: -40px;
//   // }

//   .btn {
//     height: 40px;
//     display: flex;
//     align-items: center;
//     justify-content: center;
//   }

//   .separator {
//     margin: 24px 0;
//   }

//   .accessory {
//     display: grid;
//     align-items: center;
//     grid-auto-flow: column;
//     max-width: 180px;
//     margin: 0 auto;
//     column-gap: 4px;
//     font-size: 18px;
//     color: var(--healthcare-grey-dark);

//     &-separator {
//       color: var(--healthcare-grey-dark);
//     }

//     &__cta:hover {
//       color: var(--healthcare-primary);
//     }
//   }
// }
</style>
