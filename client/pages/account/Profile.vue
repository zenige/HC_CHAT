<template>
  <div>
    <userProfile
      :user="user"
      :statusEditable="false"
      :onDelete="handleDelete"
      :onChangePassword="handleChangePassword"
      @onSubmit="handleSubmit"
    />
  </div>
</template>

<script>
export default {
  layout: 'noHeaderLayout',
  data: () => ({
    user: {
      id: '',
      name: '',
      email: 'nuiwitclup@gmail.com',
      firstname: '',
      lastname: '',
      birthdate: new Date(),
      // position: USER_POSITION.TEACHER,
      isActive: true,
    },
  }),
  components: {
    userProfile: () => import('~/components/user/UserProfile.vue'),
  },
  computed: {
    // user() {
    //   return { ...this.$auth.user }
    // },
  },
  methods: {
    async handleSubmit(values) {
      const { file, ...payload } = values

      // await this.$store.dispatch('user/updateMe', payload)

      // if (file) {
      //   await this.$store.dispatch('user/uploadImageMe', file )
      // }
      this.$bvToast.toast('Successfully update profile', {
        variant: 'success',
        toaster: 'b-toaster-bottom-left',
        noCloseButton: true,
      })
      console.log('saved' + values)
    },
    handleDelete() {
      // this.$store.dispatch('modal/openDeleteModal', {
      //   text: 'User',
      //   onConfirm: async () => {
      //     try {
      //       await this.$store.dispatch('user/deleteMe')
      //       await this.$auth.logout()
      //       await this.$router.push(this.localePath('/login'))
      //       window.location.reload()
      //     } catch (_) {}
      //   },
      // })
      console.log('saved')
    },
    handleChangePassword() {
      // this.$router.push(this.localePath('/change-password'))
      console.log('changed password')
    },
  },
}
</script>
