<template>
  <form
    class="register col-12 col-md-8 col-lg-5"
    method="post"
    @submit.prevent="handleSubmit"
  >
    <div class="card m-0">
      <div class="card-body p-3">
        <div class="text-center mb-3">
          <span class="pt-2 txt_title">{{ $t('register.title') }}</span>
        </div>
        <div class="form-group">
          <span class="helper-text error">{{ $t(errors.email) }}</span>
          <input
            v-model="values.email"
            type="text"
            name="email"
            class="form-control border-gray border"
            :class="{ border_red: errors.email }"
            :placeholder="$t('common.email')"
            @blur="validate('email')"
            @keyup="validate('email')"
          />
        </div>
        <div class="personal-information">
          <div class="form-group">
            <span class="helper-text error">{{ $t(errors.firstname) }}</span>
            <input
              v-model="values.firstname"
              type="text"
              name="firstname"
              class="form-control border-gray border"
              :class="{ border_red: errors.firstname }"
              :placeholder="$t('common.firstName')"
              @blur="validate('firstname')"
              @keyup="validate('firstname')"
            />
          </div>
          <div class="form-group">
            <span class="helper-text error">{{ $t(errors.lastname) }}</span>
            <input
              v-model="values.lastname"
              type="text"
              name="lastname"
              class="form-control border-gray border"
              :class="{ border_red: errors.lastname }"
              :placeholder="$t('common.lastName')"
              @blur="validate('lastname')"
              @keyup="validate('lastname')"
            />
          </div>
        </div>
        <div class="form-group">
          <DatePicker
            placeholder="Birthdate"
            v-model="values.birthdate"
          ></DatePicker>
        </div>
        <div class="form-group">
          <span class="helper-text error">{{ $t(errors.password) }}</span>
          <div class="input-group">
            <input
              v-model="values.password"
              class="form-control border-gray border border-right-0"
              :class="{ border_red: errors.password }"
              name="password"
              :placeholder="$t('common.password')"
              :type="isShowPassword ? 'text' : passwordFieldType"
              @blur="validate('password')"
              @keyup="validate('password')"
            />
            <span class="input-group-append">
              <span
                class="
                  form-control
                  input-group-text
                  form_border_grey
                  text-black-50
                  rounded-left-0
                  toggle-icon-wrapper
                "
                :class="{ border_red: errors.password }"
                role="button"
                @click="switchShowPassword()"
                ><i
                  :class="[
                    'password-toggle-icon',
                    { 'icon-eye ': isShowPassword },
                    { 'icon-eye-blocked': !isShowPassword },
                  ]"
                ></i>
              </span>
            </span>
          </div>
        </div>
        <div class="form-group">
          <span class="helper-text error">{{
            $t(errors.confirmPassword)
          }}</span>
          <div class="input-group">
            <input
              v-model="values.confirmPassword"
              class="form-control border-gray border border-right-0"
              :class="{ border_red: errors.confirmPassword }"
              name="confirmPassword"
              :placeholder="$t('common.confirmPassword')"
              :type="isShowPassword ? 'text' : confirmPasswordFieldType"
              @blur="validate('confirmPassword')"
              @keyup="validate('confirmPassword')"
            />
            <span class="input-group-append">
              <span
                class="
                  form-control
                  input-group-text
                  form_border_grey
                  text-black-50
                  rounded-left-0
                  toggle-icon-wrapper
                "
                :class="{ border_red: errors.confirmPassword }"
                role="button"
                @click="switchShowPassword()"
                ><i
                  :class="[
                    'password-toggle-icon',
                    { 'icon-eye ': isShowPassword },
                    { 'icon-eye-blocked': !isShowPassword },
                  ]"
                ></i>
              </span>
            </span>
          </div>
          <div class="description">
            {{ $t('common.passwordDescription') }}
          </div>
        </div>
        <!-- <div class="tnc tnc__wrapper">
          <div class="custom-control custom-checkbox py-2">
            <input
              id="accept"
              v-model="isAccepted"
              type="checkbox"
              class="custom-control-input"
              name="accept"
            />
            <label
              class="custom-control-label custom-control-accept-label pl-2"
              for="accept"
            >
              <small class="accept-tnc"
                ><span
                  ><span class="txt_black"
                    >{{ $t('register.acceptTnc') }}
                  </span>
                  <a href="#" class="txt_red" @click="openTncModal">{{
                    $t('register.tnc')
                  }}</a>
                  <a>{{ $t('register.and') }}</a>
                  <a href="#" class="txt_red" @click="openPrivacyModal">{{
                    $t('register.privacy')
                  }}</a></span
                ></small
              >
            </label>
          </div>
        </div> -->
        <div class="px-4">
          <div class="form-group px-4 px-md-5">
            <button
              type="submit"
              class="register__btn-submit btn btn_vla_red btn-block"
            >
              {{ $t('register.registerCTA') }}
            </button>
          </div>
        </div>
        <!-- <div class="col-12 pb-3">
        <div class="form-group mb-0">
          <a href="#" class="btn btn-block btn_vla_red_light_border h2dot5">{{ $t('register.signUpWithGoogle') }}</a>
        </div>
      </div>
      <div class="col-12 pb-3">
        <div class="form-group mb-0">
          <a href="#" class="btn btn-block btn_vla_red_light_border h2dot5">{{ $t('register.signUpWithApple') }}</a>
        </div>
      </div> -->
        <slot></slot>
      </div>
    </div>
  </form>
</template>

<script>
import { passwordShape } from '@/helpers/validations/authentication'
// import VueRecaptcha from 'vue-recaptcha'
import * as Yup from 'yup'

const schema = Yup.object().shape({
  email: Yup.string()
    .required('validation.email.required')
    .email('validation.email.invalid'),
  firstname: Yup.string().required('validation.firstName.required'),
  lastname: Yup.string().required('validation.lastName.required'),
  birthdate: Yup.date(),
  password: passwordShape,
  confirmPassword: Yup.string()
    .required('validation.password.required')
    .oneOf([Yup.ref('password'), null], 'validation.password.mustMatch'),
})

export default {
  components: {
    // VueRecaptcha,
    DatePicker: () => import('~/components/DatePicker.vue'),
  },
  props: {
    onSubmit: {
      type: Function,
      default: () => {},
    },
  },
  data() {
    return {
      values: {
        email: '',
        firstname: '',
        lastname: '',
        password: '',
        confirmPassword: '',
      },
      errors: {
        email: '',
        firstname: '',
        lastname: '',
        password: '',
        confirmPassword: '',
      },
      passwordFieldType: 'password',
      confirmPasswordFieldType: 'password',
      // isAccepted: false,
      isRecaptchaVerified: false,
      isShowingTncModal: false,
      isShowingPrivacyModal: false,
      isShowPassword: false,
    }
  },
  methods: {
    openTncModal() {
      this.isShowingTncModal = true
    },
    closeTncModal() {
      this.isShowingTncModal = false
    },
    openPrivacyModal() {
      this.isShowingPrivacyModal = true
    },
    closePrivacyModal() {
      this.isShowingPrivacyModal = false
    },
    handleVerifyRecaptcha() {
      this.isRecaptchaVerified = true
    },
    handleExpiredRecaptcha() {
      this.isRecaptchaVerified = false
    },
    switchShowPassword() {
      this.isShowPassword = !this.isShowPassword
    },
    async validate(field) {
      try {
        await schema.validateAt(field, this.values)
        this.errors[field] = ''
      } catch (error) {
        this.errors[field] = error.message
      }
    },
    async handleSubmit() {
      const hasError = await this.validateFields()

      if (!hasError) {
        this.$emit('onSubmit', {
          ...this.values,
          birthdate: new Date(this.values.birthdate).toISOString(),
        })
      }
    },
    async validateFields() {
      for (const field of Object.keys(this.values)) {
        await this.validate(field)
      }

      return Object.values(this.errors).some(Boolean)
    },
  },
}
</script>

<style lang="scss">
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.625rem;
  margin-bottom: 15px;
  box-shadow: 0 1px 2px rgb(0 0 0 / 5%);
}

.txt_title {
  font-family: 'Prompt-Medium';
  font-size: 24px;
  line-height: 33px;
  color: #333333;
}

.form-control {
  font-size: 20px;
  line-height: 27.5px;
  height: 3rem;
  border-radius: 8px;
}

.register {
  &.container {
    margin: 0 auto;
    padding: 20px 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  &__wrapper {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 450px;
  }

  &__title {
    margin-bottom: 24px;
  }

  &__btn-submit {
    max-width: 270px;
    font-size: 20px;
    line-height: 27.5px;
  }

  .password-toggle-icon {
    color: #ccc;
    margin-right: 16px;
    cursor: pointer;
  }

  .description {
    font-size: 16px;
    text-align: left;
    margin-top: 16px;
    color: var(--vlearn-grey-dark);
  }

  .separator {
    margin: 24px 0;
  }

  .toggle-icon-wrapper {
    border-left: none !important;
  }

  .personal-information {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    align-items: flex-end;
    column-gap: 16px;
  }

  .btn {
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .tnc {
    &__wrapper {
      margin-bottom: 16px;
    }
  }

  .recaptcha {
    &__wrapper {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
    }
  }

  .custom-checkbox .custom-control-accept-label::before {
    border-radius: 5px !important;
  }

  .txt_red {
    &,
    &:hover {
      color: #cc0000;
    }
  }

  .accept-tnc {
    vertical-align: top;
  }
}
</style>
