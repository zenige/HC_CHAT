<template>
  <form class="login col-12 col-md-7 col-lg-5 px-3 my-auto" method="post">
    <div class="card m-0">
      <div class="card-body p-3">
        <div class="text-center mb-3">
          <div class="pt-2 txt_title">{{ title }}</div>
        </div>
        <span
          v-show="showInvalid"
          class="alert alert_warning text-center"
          role="alert"
        >
          Invalid email or password
        </span>
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
        <div class="form-group">
          <span class="helper-text error">{{ $t(errors.password) }}</span>
          <div class="input-group">
            <input
              v-model="values.password"
              class="form-control border-gray border border-right-0"
              name="password"
              :placeholder="$t('common.password')"
              :class="{ border_red: errors.password }"
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

        <div class="px-4">
          <div class="form-group px-4 px-md-5">
            <button
              type="submit"
              class="login__btn-submit btn btn_vla_red btn-block"
              style="height: 2.5rem"
              @click.prevent="handleSubmit"
            >
              {{ $t('login.loginCTA') }}
            </button>
          </div>
        </div>
        <slot></slot>
      </div>
    </div>
  </form>
</template>

<script>
import * as Yup from 'yup'

const schema = Yup.object().shape({
  email: Yup.string()
    .required('validation.email.required')
    .email('validation.email.invalid'),
  password: Yup.string().required('validation.password.required'),
})

export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    // onSubmit: {
    //   type: Function,
    //   default: () => {},
    // },
    showInvalid: {
      type: Boolean,
      default: false,
    },
    errors: {
      type: Object,
    },
    values: {
      type: Object,
    },
  },
  data() {
    return {
      passwordFieldType: 'password',
      isShowPassword: false,
    }
  },
  methods: {
    async logined(e) {
      // console.log('logined')
    },

    async validate(field) {
      try {
        await schema.validateAt(field, this.values)
        this.errors[field] = ''
      } catch (error) {
        this.errors[field] = error.message
      }
    },
    switchShowPassword() {
      this.isShowPassword = !this.isShowPassword
    },
    async handleSubmit() {
      const hasError = await this.validateFields()

      if (!hasError) {
        await this.logined()
        // this.$emit('onSubmit', { ...this.values })
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
.login {
  &.container {
    margin: 0 auto;
    padding: 0 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  &__wrapper {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 440px;
  }

  &__title {
    margin-bottom: 24px;
  }

  &__btn-submit {
    margin: 0 auto;
    max-width: 260px;
    height: 40px;
  }

  .toggle-icon-wrapper {
    border-left: none !important;
  }

  .password-toggle-icon {
    margin-right: 16px;
    cursor: pointer;
    color: #ccc;
  }

  .alert_warning {
    color: #ffffff;
    background-color: #cc0000;
  }

  .alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    margin-bottom: 1rem;
    border: 0 solid transparent;
    border-radius: 0.3125rem;
  }
}

.txt_title {
  font-family: 'Prompt-Medium';
  font-size: 26px;
  line-height: 33px;
  color: #333333;
}

.card {
  border-radius: 0.625rem;
  margin-bottom: 15px;
  margin-top: 5px;
  border: 1px solid rgba(0, 0, 0, 0.125);
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  box-shadow: 0 1px 2px rgb(0 0 0 / 5%);
}

.form-control {
  height: 3rem;
  border-radius: 8px;
}

.login__btn-submit {
  font-family: 'Prompt-Regular';
  font-size: 20px;
  line-height: 27.5px;
  color: #fff;
}

.login__btn-submit:hover {
  background-color: #ffffff;
  color: #10c4cc;
}
</style>
