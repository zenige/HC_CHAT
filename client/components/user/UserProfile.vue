<template>
  <form
    method="post"
    class="user-profile vl_navbar"
    @submit.prevent="handleSubmit"
  >
    <div class="">
      <div class="container pt-4 pt-md-4 pb-4">
        <div class="row">
          <div class="col-12 text-center py-3 py-md-3">
            <div class=""></div>
          </div>
        </div>
      </div>
    </div>
    <div class="">
      <div class="container pt-4 pt-md-4 pb-0">
        <div class="row">
          <div class="col-12 col-md-6 offset-md-3 position-relative">
            <div
              class="
                position-absolute
                left-0
                right-0
                d-flex
                justify-content-center
              "
              style="padding-top: 20px"
            >
              <div
                tabindex="500"
                class="
                  btn btn-file
                  p-0
                  position-relative
                  circle_user_100p
                  overflow-hidden
                  position_user
                  shadow-0
                "
              >
                <div
                  class="
                    position-absolute
                    z-index99
                    w-100
                    hover_img_upload
                    d-flex
                    align-items-center
                    justify-content-center
                  "
                >
                  <div class="txt_w">Add photo</div>
                </div>
                <img
                  :src="previewUrl ? previewUrl : defaultPreview"
                  class="img-fluid"
                />
                <input
                  type="file"
                  class="file-input"
                  data-browse-class="btn p-0  rounded-circle"
                  data-show-remove="false"
                  data-show-caption="false"
                  data-show-upload="false"
                  data-fouc=""
                  @change="handleFileChange"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="row pt-5 pt-md-5">
          <div class="col-12 col-md-6 offset-md-3">
            <div class="d-flex justify-content-between">
              <div class="txt_vl_head txt_profile_head">User Profile</div>
              <!-- <div v-if="statusEditable">
                <div
                  class="
                    form-check
                    form-check-switchery
                    form-check-inline
                    form-check-right
                  "
                >
                  <label class="form-check-label">
                    <span class="txt_vla_title_grey">{{
                      isActive ? 'Enable' : 'Disable'
                    }}</span>
                    <input
                      v-model="isActive"
                      type="checkbox"
                      class="form-check-input-switchery"
                      data-fouc=""
                      data-switchery="true"
                      style="display: none"
                    /><span
                      class="switchery switchery-default"
                      :class="{ checked: isActive }"
                      ><small class="knob"></small
                    ></span>
                  </label>
                </div>
              </div> -->
            </div>
            <div>
              <hr class="mt-1 mb-3" />
            </div>
            <div class="row">
              <div class="col-4 pb_me-4 d-flex align-items-center">
                <div class="txt_vla_title_grey">Email</div>
              </div>
              <div class="col-8 pb_me-4 d-flex align-items-center">
                <input
                  v-if="emailEditable"
                  v-model="_user.email"
                  type="text"
                  class="form-control border-gray border"
                />
                <div v-else class="txt_vla_grey_43 py-2">{{ _user.email }}</div>
              </div>
              <div class="col-4 pb_me-4 d-flex align-items-center">
                <div class="txt_vla_title_grey">First name</div>
              </div>
              <div class="col-8 pb_me-4 d-flex align-items-center">
                <input
                  v-model="_user.firstname"
                  type="text"
                  class="form-control border-gray border"
                />
              </div>
              <div class="col-4 pb_me-4 d-flex align-items-center">
                <div class="txt_vla_title_grey">Last name</div>
              </div>
              <div class="col-8 pb_me-4 d-flex align-items-center">
                <input
                  v-model="_user.lastname"
                  type="text"
                  class="form-control border-gray border"
                />
              </div>
              <div class="col-4 pb_me-4 d-flex align-items-center">
                <div class="txt_vla_title_grey">Birthdate</div>
              </div>
              <div class="col-8 pb_me-4 d-flex align-items-center">
                <div class="form-group mb-0 w-100">
                  <div class="input-group">
                    <DatePicker
                      :value="_user.birthdate"
                      placeholder="Birthdate"
                      @change="handleDateChange"
                    ></DatePicker>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="">
      <div class="container pt-3 pt-md-3 pb-0">
        <div class="row">
          <div class="col-12 col-md-6 offset-md-3">
            <!-- <div class="row">
              <div v-if="_user.position" class="col-4 pb_me-4 d-flex align-items-center">
                <div class="txt_vla_title_grey">Position</div>
              </div>
              <div v-if="_user.position" class="col-8 pb_me-4 d-flex align-items-center">
                <div class="form-group mb-0 w-100">
                  <select v-model="_user.position" class="form-control border-gray border">
                    <option v-for="position in positionOption" :key="position.label" :value="position.value">
                      {{ position.label }}
                    </option>
                  </select>
                </div>
              </div>
            </div> -->
            <div class="row d-flex justify-content-center">
              <div class="col-8 col-md-6 col-xl-6 py-3">
                <div class="form-group mb-0">
                  <button
                    type="submit"
                    class="btn btn_vla_red btn-block h2dot5"
                  >
                    Save
                  </button>
                </div>
              </div>
            </div>
            <div class="row d-flex justify-content-center">
              <div class="col-12">
                <hr class="mt-2 mb-2" />
              </div>
            </div>
            <div
              v-if="onChangePassword || onDelete"
              class="row d-flex justify-content-center py-3"
            >
              <div class="col-8 col-md-6 col-xl-6">
                <div class="form-group mb-0">
                  <button
                    type="button"
                    class="btn btn-block btn_vla_red_light_border h2dot5"
                    @click="onChangePassword"
                  >
                    Change password
                  </button>
                </div>
                <!-- <div v-if="onDelete" class="text-center pt-3">
                  <span
                    class="txt_vla_title_grey delete-btn"
                    role="button"
                    @click="onDelete"
                    >{{
                      permanent ? 'Permanently delete user' : 'Delete user'
                    }}</span
                  >
                </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- <div v-if="user.workspaces && user.workspaces.length > 0">
        <div class="container pt-3 pt-md-3 pb-5 plr_15p">
          <div class="row">
            <div class="col-12 col-md-6 offset-md-3">
              <div class="d-flex justify-content-between">
                <div class="txt_vl_head">Workspace</div>
              </div>
              <div>
                <hr class="mt-1 mb-3" />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-12 col-md-6 offset-md-3">
              <div class="table-responsive">
                <div class="table-responsive" style="overflow-y: hidden">
                  <table class="table text-center table_kpi_border_bottom table_hover">
                    <thead>
                      <tr class="bg_kpi_grey_f3">
                        <th class="m_width_50p">No.</th>
                        <th class="m_width_80p">Workspace ID</th>
                        <th class="m_width_110p">Workspace name</th>
                        <th class="m_width_50p">Type</th>
                        <th class="m_width_50p">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(workspace, index) in user.workspaces" :key="workspace.id">
                        <td data-columns="group-test-col-0" class="text-center">{{ index + 1 }}</td>
                        <td class="text-center">{{ workspace && workspace.id }}</td>
                        <td class="text-left">{{ workspace && workspace.name }}</td>
                        <td class="text-left workspace-type">{{ workspace && workspace.type }}</td>
                        <td class="text-left">{{ workspace && workspace.isActive ? 'Enable' : 'Deleted' }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div> -->
    </div>
  </form>
</template>

<script>
// import { USER_POSITION } from '@/constants/user'
import defaultPreview from 'assets/hc-libs/images/main/face_default.png'
import dayjs from 'dayjs'

export default {
  components: {
    DatePicker: () => import('~/components/DatePicker.vue'),
  },

  props: {
    user: {
      type: Object,
      default: () => ({
        id: '',
        name: '',
        email: '',
        firstname: '',
        lastname: '',
        birthdate: new Date(),
        position: USER_POSITION.TEACHER,
        isActive: true,
      }),
    },
    onChangePassword: {
      type: Function,
      default: undefined,
    },
    onDelete: {
      type: Function,
      default: undefined,
    },
    statusEditable: {
      type: Boolean,
      default: true,
    },
    emailEditable: {
      type: Boolean,
      default: false,
    },
    // permanent: {
    //   type: Boolean,
    //   default: false,
    // },
  },
  data: () => ({
    previewUrl: undefined,
    imageFile: undefined,
    defaultPreview,
    // positionOption: Object.values(USER_POSITION).map((type) => ({ label: type, value: type })),
    isActive: true,
    _user: {},
  }),
  created() {
    const { user } = this

    this._user = {
      ...user,
      birthdate: dayjs(this.user.birthdate).format('DD MMMM, YYYY'),
    }

    this.previewUrl = user && user.image && user.image.url
    this.isActive = user.isActive !== undefined ? user.isActive : this.isActive
  },
  methods: {
    handleSubmit() {
      let payload = {
        firstname: this._user.firstname,
        lastname: this._user.lastname,
        birthdate: new Date(this._user.birthdate).toISOString(),
        email: this._user.email,
        file: this.imageFile,
      }

      if (this.statusEditable) {
        payload = { ...payload, isActive: this.isActive }
      }

      this.$emit('onSubmit', payload)
    },
    handleFileChange(event) {
      const { files } = event.target

      if (files) {
        const [file] = files
        this.previewUrl = URL.createObjectURL(file)
        this.imageFile = file
      }
    },
    handleDateChange(event) {
      this._user.birthdate = event.target.value
    },
  },
}
</script>

<style lang="scss">
.txt_profile_head {
  font-weight: bold;
}

.user-profile {
  .table-responsive {
    min-height: auto;
  }

  .form-check-switchery .switchery {
    top: 6px;
  }

  .img-fluid {
    object-fit: cover;
    height: 100%;
    width: 100%;
  }

  select {
    &.form-control {
      text-transform: capitalize;
    }
  }

  .workspace-type {
    text-transform: lowercase;

    &:first-letter {
      text-transform: capitalize;
    }
  }

  .delete-btn {
    cursor: pointer;

    &:hover {
      color: var(--vlearn-primary);
    }
  }
}
</style>
