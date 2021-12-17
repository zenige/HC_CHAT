<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    modal-class="patient-info-modal"
    hide-footer
    @close="onCancel"
    @hidden="onCancel"
  >
    <template v-slot:modal-header="{ close }">
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">
          รายละเอียดเพิ่มเติม
        </h4>
        <button
          type="button"
          class="close pr-1 pt_15p"
          data-dismiss="modal"
          @click="close()"
        >
          <img
            src="~assets/hc-libs/images/main/ic_close_grey.svg"
            width="37"
            loading="lazy"
          />
        </button>
      </div>
    </template>

    <template>
      <div class="modal-body px-3 px-md-3">
        <div class="d-flex flex-column justify-content-start">
          <div class="txt_patientInfo_16px">ข้อมูลส่วนตัว</div>
          <div class="txt_patientInfo_13px">
            ชื่อ-นามสกุล: {{ userInfoDataModal.Fullname }}
          </div>
          <!-- <div class="txt_patientInfo_13px">เพศ: ชาย</div> -->
          <div class="txt_patientInfo_13px">
            ช่วงอายุ: {{ formatAge(userInfoDataModal.Age) }}
          </div>
          <div class="txt_patientInfo_13px">
            วัน/เดือน/ปี เกิด: {{ userInfoDataModal.DateOfBirth }}
          </div>
          <div class="txt_patientInfo_13px">
            เบอร์โทรศัพท์: {{ userInfoDataModal.Tel }}
          </div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            Group: <span>{{ userInfoDataModal.Group }}</span>
          </div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            รูปภาพ
          </div>
          <b-container fluid class="p-2">
            <div :class="['sectionImg', { activeShowMore: showMore === true }]">
              <div v-for="(item, index) in userImage" :key="index">
                <b-img
                  @click="showModalImg(index, item.src)"
                  thumbnail
                  fluid
                  :src="item.src"
                  :alt="item.alt"
                  :id="`Img${index}`"
                ></b-img>
                <div :id="`ImgModal${index}`" class="userImgModal">
                  <font-awesome-icon
                    @click="closeModalImg(index)"
                    class="close-img-modal"
                    icon="times"
                  />
                  <!-- <span class="close-img-modal">&times;</span> -->
                  <img class="img-modal-content" :id="`modalImg${index}`" />
                </div>
              </div>
            </div>
            <div class="show-more pt-2 mx-auto" style="max-width: 50%">
              <button
                class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                style="margin: 0 auto"
                v-if="!showMore && this.userImage.length > 3"
                @click="setShowmore()"
              >
                แสดงเพิ่มเติม
              </button>
              <button
                class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                style="margin: 0 auto"
                v-else
                @click="setShowmore()"
              >
                แสดงน้อยลง
              </button>
            </div>
          </b-container>
        </div>
      </div>
    </template>
    <SkinDiseaseImgModal
      :isOpen="isShowImgModal"
      :onCancel="closeShowImgModal"
      :imgModal="imgDataModal"
    />
  </b-modal>
</template>

<script>
import VueEasyLightbox from 'vue-easy-lightbox'
import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTimes)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VueEasyLightbox)

export default {
  components: {
    SkinDiseaseImgModal: () =>
      import('~/components/dashboard/UserImgModal.vue'),
  },
  name: 'patientInfoModal',
  props: {
    userInfoDataModal: {
      type: Object,
      default: () => {},
    },
    isOpen: {
      type: Boolean,
      default: false,
    },
    onCancel: {
      type: Function,
      default: () => {},
    },
  },
  data: () => ({
    isModalOpen: false,
    isShowImgModal: false,
    showMore: false,
    imgDataModal: {
      src: null,
    },
    userImage: [
      {
        src: 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQEBUREBIVFhUVFRUVFRcVFRgVFRUWFRUWFxUXFRUYHSggGBolGxUVITEiJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFxAQGy0lHyUtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBIgACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAAABAECAwUGBwj/xABJEAABAgIFBgoHBgYBAwUAAAABAAIDEQQSITFRE0FhcZGTBRQiMlKBobHR4gYVQlRikqJygsHS4fAjM1NjlLJDc4PxBzR0wvL/xAAaAQADAQEBAQAAAAAAAAAAAAAAAQIDBAUG/8QAOREAAgEBAwgIBQQCAwEAAAAAAAECEQMSEwQFITFRUpHwFEFhobHR0uIVMnGBkiLB0+FiciNC8VP/2gAMAwEAAhEDEQA/APjkkSV7MO1FmHauy6bVKqJLSzDtUWYdqd0KlJIktLMO1TZh2ouhUykiS1sw7VFmHai6KpWShXsw7VNmHandCpSSJK9mHaizDtRdCpSSJLSzDtUgDDtRdCpmArBq0AGCsGjBUoFGNVTVW4aMFIYMFeGNJi9VTVTNQYIqDBPDHdYrVRVTFTQgtGCMMVGLSUSW5aMFBboU3CTGSJLWQwRLQpukmUkLSQU1RgigVM5IktJBEtCKCqZyRJay0KZJ3QqZyRJXkrSRdFeMpK0leqiqndCpSqiS0qoqq0hVFZKZK8lMlF0szkiS0kokldEUkrSUyVpIuhUpJTJXkoki6FStVEleSKqdBVKSUyWoapDU6BUyDVYNWgarhitRKTMwxXDFo1i7HAvA+WNZ1jBtccBo0/sbWdk5uiN7KDm1GJz6DwdEjGUNs8Tc0ayu9RfRZo/mPJ0NsG039i9BDhtaA1oAAuAuV16lnkkI69PgetZ5JCPzafA5TfR+jD2CdcR/4FVi+jlHNwc3U4n/AGmuuhbYNnurgb4Fnuo8pTPRh7bYTg/QbHdRuPYuFFglpLXAgi8GwhfSJJPhLg5kdsnWOHNcLx4jQua1yOLX6DltsjTVYcOf7Pn5YqFi6NMobobixwtGwjMRoSzmLzZQadGeTNNOjFixRVW5aq1Vk0YtmVVRVW9RFRKhNTGqpqrWSkNSFeMaqmqtQxWqIFeMaqmqtqisGJ0FeF6isGLeopqJoV4XkiqmKiKiod451VEk3xR2jaFPFHaNoUaB4i2itVFVNcUdo2hHFHaNoRoFfW0WqoqprijtG0IFFdo2hPQO+qVFQ1WDUzxV2jaFPFXaNqVUTiLaK1VNVNcVdo2qRRXfsp6BYi2i9RAYmuLO/ZVxRj+yhUC+toqGK7WLdtHN1m0LVtHKtFqaIoNDMR7WDPecBnK9vChhjQ1okAJALh8BQqpc6uwHmitPWZSOpdgRj/Vg7D4r0smlCEavW/p5ns5FaWcI1b0vtWriboWGWP8AVg7D4qMsf6sHYfFdPSIcteZ2PKrPb3rzN0LDLn+rB2HxQIx/qwdh8UY8OWvMXTLPb3rzGELARj/Vg7D4qcsf6sLYfFHSIcteZfSrPb3rzFOG6DlYcwOU20aRnC8k6Gvb5c/1YOw+K8zS6LJ7gJETsIuttsXDlThJqS+55eXShJqUfvqOWWKKidMAquQK4meXK0W0SqKaibyBRkCoqZ30KCGpqJvIFTkCgV8VyasIaZEEqwglFSb4sIakQ00ISsIKAvoTENTk04IKnIpiviWTRk07kUZFUmF85XFx0xsd4KeLjpjY7wTFU/FtRVPxbVBd4X4uOmNjvBTxcdMbHeC3qn4tqiI0yPP2/ohuiqCkJubKcnN659yyfEkJGczdIbVpEo9lgNmeefSblnDhlxkSAR1rFNyejX9uGqn/AId9lFaaFoBdc+Q02mYzXBNshA+0O3wWbIpBkbP3mTsNv2p57b1sn1V8zDKHTqMRAHSGw+CsIA6Q2HwW4Z9rapDNe1M5L4uII6Q2HwUuhyFhnoE/xTIZr2rCmMmJEulntv0XdgSk6IcJVaQhHeRmkRaJGdiiHSnucJHkytBsl4rGksLTcQtoL8nJ1kjnlZ1qYy01Wrnls9WMY3Uz3XooHuhWGIBWJnDax7SbAbS0mdy7ogP6cfdQ/wAiR9BoAiw3ioa4dbKM+GCCBKxthtnpXr2cDu6Dv8qL4rqWUUSOTpMou6tFOedR5/IP6cfdQ/yKpgROnH3UP8i9N6lPQd/lRfFQeBXdB3+VF8UulLaN5VLazzWRidOPuof5EZGL04+6h/kXpPUzug7/ACovip9SnoO/yovin0rtIWUz2nmxR4nTj7qH+RW4vE6cfdQ/yL0g4FPQd/lRfFaN4FPQd/lRfFS8q7TRZVLaeY4tE6cfdQ/yLxXpYHNjkVnWtaZvaGuN4uAFlmC+vjgU9B3+VF8V8r9NKE1lIigznWmeW54uBlXdbZMCeaWZZzyuq2mtlaO1ldb/AH5566J+KiUx4kJnaUxQKpJ5085bOXXK8peNDaDMNJkTOZnd2FXojHkEthh0rbgSJ4Ceu5DcqO815dmo0t1+l9XPDvOyyGCJzmr5LSp4Pk5gIz2+N+nMmsmoUtB40nRtMVySkQk2IasIaKk3jm0gSBA23AYTJ/BcGLS4kN4k4nEXheh4TggyD3ENvk285uoW3nQuDTYMIOsY4WG92fZPqTalKFI7TuydJxpSteeunh9RdtLcXz02H2rRJd7gqKXclwdMWOJtE5Ttna3uXBZM81sw27RPvXX4Niub/EDBISygYJGRBImJ6ZjrtvUzm18zT7jTKVVdXOo7QhIySbhtDgHC4iY1FWySKnl1EsmoySeySrk1VQqcbib+idhRxN/ROwr2XFKT0PqgeCOKUnofVA8FydL/ANfyO7oWV7j4S9J43ib+idhQaE/ou2Fey4pSeh9UDwRxSk9D6oHgjpX+v5B0LK9x8Jek8Kzg6I5xL2mQJDRI3DOoo1CJfE5JsIF11k173ilJ6H1QfBcj0fgRnGkFot4xEDuVCFrTK4jDCxQ7dNxbu6Ht7H2GscnyxKX6WtGjRLav8dlf3POUvg1xAIYeSQbAZyBtkm2UQysadhXsOJ0noDbB8FWJR47RWcGtAvLnQQNpCuOUJOqu/kZzyXLJLTB8Jek8oKM7onYVYUZ3ROwrtDhWHOWWhfPBltlJSeE4Y/5oO9o/ctceWxcf6MOiZRu90vScUUY4HYqUmjvDXOY0l0uSJZ/33J+lelEFlxLz8DWEbS0BcLhD0ujPmIcmD7ILttWzq2rT/ketJff+hQyW2r1d/kL06C2FVDjWfOs4HAC7USRrkkmUu3miWDRZdZIFKViQ4kzNnaVRidnRuaf0r9k/Fnq2UbqVXV7f61HrfR70sfQ3k5KE9pABD24XFpnYV9C4B/8AUegReTSYTIDscjlYfzNNYfL1r45R4jPad2HwTEQQMzj90Ej6lpaWMZKqpx5R0RyKxtI3tCf1o/I+/wBH9JeCnmQpVDH2odQbXkBdcij1a5dRqptDsmKu2tJfmVrWH/k2sK2bAcbA5v1eCw6K3qZHwty+WXg/Bo+9070o4Lg2PpNFJ/twTF25MmXWsG+mHBVWtloUv/ivHevhghw28+IDo/dq1fTIJsJn1GXcqWSwXzPwN4ZrsEv+Sen6xX7M916T/wDqK5xLKFDhQ2z/AJhhNyjtTXVg0bTqXlGelFMa8xMu+eeZm35CKo2LlxosH2W1j9t0klFiE84SGhXhxitBs7KxsVdik+/i2jucNel9MpUMQ4sQVMGMYyt9uq0VtRsXKoNMfMQy7kG+sTVDQCXXayUg4rMrJrZoOa+k9C0bNXP2OnTqfDc0VWkGRFt0piUpaAs4NOdCc0tA5IIN/KmTf+8wSJVoomZ6u5JQ0qK2PxXmYTSkqPmtTv0Ph+ECa8MtmZktNYTxlZJd+iRGRW1oZDho7iMxXzwhNcH8IRaO6vBfVMpGwEEaQQQUNs4bXI09MND7dXme/EJXEJcGgenEUWR2NcMWNa12wiR7F6GhektGi3RGNOEQNh9rhLtUOUl1d/8ARxvJbZdXi/BMWi0MFwdKbrhO4HMTqt2nFc13o2HsbXd/ErVnOE7QTymjxxXuoVFivFZrWuBuLTDIPWFoKDH6A+hZvKE1Sq6uvYarJ8siv0wl+M/T3HzL0co7jGE28gtiC6Yk1wEtsl36LwZkoxc0ch8M/dIIs0gz6pHFdH0Mo0V1HdVaCBHjdG8OtvXd4jG6DfoU49dbVfqXbWOUzk3GDpq1SdeuvynBbBkJDNYpya73EY3QH0KeIxugPoTx1tXEw6HlP/zfCXpPPmGq5NehNBjdEbWKnEo/QH0KsdbVxDoeU7j4S9JGUh/Cq5SH8K6oZR/7W1qnJ0f+19K83Hgtp9d0m2/x4M5WUh/CjKQ/hXVydH/tfQqxOLNBc50EAWkksAGso6RDtDpFtsjwZzhEh/CuJ6LuYDSZy/8Adxpaq2ZM8KemNAhTEJmWd8DA1nW9w7gV4WlcLxyHGF/DbFiRIhayUwS64OlWAGiS6IRcmk01Xb9H9zOWVWuvRwPacP8ApNR6KKoAiRMzBcNLzm1X96+a8JcJRaTEykZ0zmAsa0YNGYKpgHOqmAV32cYWWlazltrW0tfm1bDEvKBEOha5A4FRxc4LTpL2+JjdZkXlQtjBOCjInBJ26ethdZDOa7q71mmYcI1Xam/7LLIlZwtY1l9f2Q7rKAqa6vkCpyJ0q8YaTIEYodFJvJ2oyRwKMkcDsRjLrZVZFAomtMkcFIhHBLFiLSZrRrypyZwU5I4FUrWKHpWoCwalR0Mq4acCrhxwOxaq1sXr0CekUdNXebeodwTBOg7EZMWTGYY4BZOVnfVJdT8V9SbgrNFiY4uFBopVuf0YXWLyClacVcji7sFGJTqFdZtwbwjFozxEgOLXZ5XO0OabHDWvpvo16eUePJlJDYMTE/ynaieZqO1fLeLnBTxc4LG1jG1+biXZucPl8EfWvQGKwUV85W0iORdcX2L0uWh/CvhVApseBIwYj2X802G03tuPWvScG+nlLhyEaHDjDS0Q3/M0S+lccrGqvJ1KVraJUVKfQ+pZWH8Kgxofwrz/AAP6Z0CPY/8AgOwigBvVEFm2S9EHQDaHQ5faauaUoxdJJotTtnqu8DMxofwqhjw/hWxMHpQ9rVWcHpQ9rUK1s+0u9bf48P7PicPg44O+eH4rYcGHB3zsTLXvzUKj77zK2Xf7nR995lDjnB/9X+UfWbrLs1pfMvy9gr6rPxfPDQODHfF87E2Y0T3Kj77zKMvE9yo++8yVzOG6/wAo+sp5fmvauPtFvVr8XbyGj1c/F28hpnLxfc6PvvMjLxPc6PvvMpws4bnfH+QPiGa95cfaLern4u3kNHq5+Lt5DTOXie50ffeZAjxPc6PvvMjCzhud8f5A6fmveXH2i/q5+Lt4xHq52Lt4xMZeJ7nR995kZaJ7nR995kYecNzvj6w+IZr3lx9ov6udi7eMR6ufi7eMTGXie50ffeZGXie50ffeZGHnDc74+sPiGa95cfaL+rn4u3jEer34u3jUzlonuVH33mUZaJ7nR995kYecNzvj6w6fmzeXH2i/q9+J3jEer34neMTGXie50ffeZGXie50ffeZGHnDc74+sPiGa95cfaL+r34u3jEer34u3jExl4nudH33mRl4nudH33mRh5x3O+PrDp+bN5cfaL+r34neMR6vfi7eMTGXie50ffeZGXie50ffeZGHnHc74+sOn5r3lx9ov6ufi/eQ0ern4v3kNMZaJ7nR995kZaJ7nR995kYecNzvj6w+IZr3lx9ov6vfi7eMR6vfi7eNTGXie50ffeZGWie50ffeZGHnDc74+sPiGa95cfaL+r34u3jFHq5+Lt7DTOXie50ffeZGXie50ffeZGHnHc74+sPiGa95cfaLern4u3jEerX4u3jEzl4nudH33mRlonudH33mRh5w3O+PrD4hmzeXH2i3q1+Lt4xHq12J3kNM5eL7nR995kZaJ7nR995kYWX7nfH+QPiGa95cfaLernYneMR6tdid4xM5aJ7nR995lIjRPcqPvvMlhZw3O+P8AIHT817y4+0V9XHTvGI9XOxdvGJnLxfc6PvvMpMaJ7lR995k8LOG53x/kD4hmveXH2ivq44neMUerD8Xzw03lonuVH33mUZeL7nR995kKzzgv+j/KPrDp+a9q4+0U9WHB3zsR6sODvnYmzHie50ffeZGUie5QN/51VzOG6/yj6w6fmveXH2CBqi8j7x/+oZNDSDc6ZwaAO2pPaEwwO9kO1mKDLXZLah0/ae7U2ILOwAdU19lU8zFe0WNQXlg+o/6EdykVTaCCMXWD/SzamGVvZDtJMQHbMSGxBB9pzydEUHaTZsmiosTtFa7M7xqaB2mp4qZCXsjSbzqmy3qCZaX3NDuqICdc5WdUkFsr3OJwEUHaZS2TTqGI9viKlzJ3hx03f6TPYpIHtOaNAFuyp3pkOebG1tQiCZ65T/BFWV7nE4CKO0y7poqGI9viLNLTY2Xef9JBBqC9wJ0XdZqd21MFznWCtoAiDwmVarK8uJwyol1n8B2IqPFe3xFZzztAHUB9F/aguYOaRrN/UKliYcXE3u0ARB2CSvVLby4uwygkPtWX6NuCdRYj2+IoGslNxEs2J+iwaVDnNOdugD/8LdxcbSXb0eC2k5ud1b/qDk9nO7tdxUMR7e5ijqjbJtnn0aOZfjsxVWNBMpt06ALSeZgmJHF29HgtCCGym6brT/EFgzC7PfsRUMXt8RN7mk2ESzavkVm1arjMZhtmeh8PatpOxdvR4LR4Ia0TdbN38wZzVw+HtTqGK9viIzZi39/cWkWpMWtta3uA6GIK2k7F29HgtIgdJlruaf8AkHTdoRUMXt8RSFVnKbbbOvN7GP4qhlo2eRNSdi7ejwWkUOMnTdbf/EHOF+bUfvIqGJ2+IqarhOYmL9Ix5m3biqNiNGdpGHhyL000uBmC7eDwVojDeC6R/uiw4eH/AJSqGK9viKOa0WhwlmPjyLCis03loOOY6+RZr/8AKZY5w6RxBiiRUuYZTBeRn/iiYOBs7c/Yio8V7fEVJDbCRqN2sEM7kAMPNcJ4WT6jUt/diZa5wsNYj/qjaDKxDoZvaXkZ/wCIJjWJdqKixO3xFa7biQNIFvWKngrDW1wHXIaqkwmK7rjWP/dExqMu9BhuvaXn/uAEaxLuSqGI9viKhzMzgO7bUUuqytqyxEu8MkmK5N9bWIoB7pH92qQx3sOedUUT6xLumioYj5qL12m5wP2pDtq/ioJYL+T1TB6izxTFYm+trEUDslLuUta72XOOjKNn1tIt6ppVDEe3xFhVN1Q6rHdQqfgguZncJ5w4fiGT7luTM21xjKKO4/ouZwpTXtIYx78TyydQsu6lla2sbKLkwxH1MvwjSajZNvN0iC2Wewt/FYQ+ExLlQwTjJo7JLnPeSZkknEmZVF5E8utHO9HQtgXntPYOhA88OGt0z8tWzrkqyhi5jjpc78AO+ad4vEHOiBut9vUL/wAEWjmvnpc/ubOW2a9a8ediCdSte10hi4Bo1cmXUEFkMey533pN7pnsTVWI4/zJk/H2C1aZFw50TqD7es3DtOhO8GKImTrKjtAB/ANvUmCwc4OngHA7TVkO1NuLyJB4AwD79ZnMqGQYhsD9PPuGJtsCLwsQUc4SkGEDAO77JnrUsgNlMtIGNa0/ZEre7Snw0tueHHS/kjUDf12aCsy15MzEt+3+qLwYooS0CTWOAz8q0jSavYFDIQJkGO+YbSZWBPsgPNpiSFxNfsFtp0KX1rmvkPt2nST+Fw7U7wYvPLEuQ3mtM+lP/Xk2a79SzqN6Lvm8qdqP6f1/qt2QnNFZz7fZBfYdJtu0Z9SL4sXnliLYbWSNU1jaBO4ZnHk7B14TzqN6Lvm8qeLHm0xPr/VGTf0/r/VO8GLzyxOFBYZktdICZ5V+A5uc2bTmVXgEklrpn4vKunGhvEmV7rXcv2sL812ueKyyb+n9f6ovA7XnliFRvRd83lWtJhtrEVTyZN53REj7OIKfo0N1cTfYDWPLvDeUc+AKzqPzv+v9UXhY2jnzOfUb0T83lWjmNqN5J5z/AGtDPh0pvJv6f1/qtRDfkzy7nD2+kDP/AFCd4Fbc8s5lRvRd83lV4UNpBbVdiOVnbOzm5xPrkm8m/p/X+qkNeDMRLreeleBW3PLOdUb0XfN5VaHVHsukbCK3lvC34WpQgCsX2Ota0OmbbwNAMxPQvOv4cpBNj5aL+9YWuVws3R6+w1s70tKO3EgtB5pIvBrXjHm/uRUMk0zDT81hGBFW0LlN9IY1QtNpvBmRI57J2zHcFnC4ejAis4kZ7we9ZdPsu3gXcnr8jtugsIm1rtIrXaRZa3uz4nNoaDMNcD9rypujxHOAeyJYbQa/ePwVOEaSITK5fI9APvOLcBjh2Dqdokqt6DFWlXRCtLiwWNLnNIOYA2OOqrYezUuK/hN1YFokARZOZP3pfgl6ZTHxXVnknATmANCWXkW+Wzk/0Oi55odkLPRpPV0ekQoorVXaSCKwOkSkf3arPgNFtUkYh1nXybOtcfgQPrza4tA50rjoTx4cOWDWuIbcXVjec88P1XdZ5UrilPR1fXnr2GEq3mlpGy5p5zCdNa3bV75oyDDzQToLgD1WSPVboT9UuvfVOIfyTrGbq2LkcK8IOg8kPrOlmfWDdcjfoW07WMFWREZuToiKVS2t5BaS7BzubpNkxqmvPx31nEqXRiZucSXOvJMzL9y2LFeRlGUO1ojrhGhLVasomqrnrRUKoe94uCee0k6H2n5VrxNo572jQA4nUeTyeu3Qm8i8WNbV6wXHW7wkFnxN+HaPFe1ePnsUxLRc1zWjRXmdZq26rtCy4uOm3Y/8qdZQHnNIYkiQ/eF604u5vMbb0jKf3RPk679SLwsQT4m0c94GgB1br5PJ69hQ9gIkHtAwAfLWeTada34m/DtCkUJ/R7Qi8LFFOLjpt2P/ACrZtDaJF7xI2gCtM/TYNOzQ4KGW3gF2EwWt19I6LsZ3LN1FeTMiZN5JHineFiir4da97ZC4APkBoFVRxcdNux/5VvC4PiC8l2ur+CZhUE85wsGaYm44D8Tm6whSB2ukUh0RoFZzmyzDl8oj7vN09WkUfBmZl7ZnQ78qciUd7jMjukBmAE7lHE3YdoTvE4onxcdNux35VtAo4by6zbLG2O52PNzX65YphlBeSABfpCvGoziZNHJbYLRbi7rNuwZkXgxhDi46bfq/Kp4sOm3Y78qb4m7DtCOJuw7QneFimEKjgNca7bg0WOvcZ9HotcFnxYdNux35V0nURwYBK8lxtFwkG9tdLtoLhOw2mdpB2WovDxRXiw6bdjvyrRlHFRwrN9l1zsxLej8aY4o7DtCDCqMe58gKt5I6bTIYmxF4Fas58WGxrS5z2gATJ5X5Vw4PDgfOUM2AmdYSlmnZYsfSHhKuKjbAc2jSuEYhlVzYYnE4rhtsralSPV3nqZPkt6FZ633GlLpDojy5xmewDADMEuhC85urqz00qKiBCFIKAOlRqa6Ayq21zrSDc3CzH9EjHjOeazySdP7sWZKhXK0bSj1LqIjZpNvrYJjJkNnK0iY0NxOu5McFUAxXTPNF+nQrcJUkOJayQaLLPaIz6sw/VVGNI3n9iJWlZ3F9xZ1JdUqNsbnle46fBLIQs229ZqklqOmzhaIIVQXiytnDdGnSuaSpBViJ2jYqlOU0qvUTGMYN0WszUqSFaLDqmRvlbo0KUXXTQzQhCQH0tsOZkLTgL1rkmt50ieiDYPtOHcNoQhesj5Ah5Lr81wuA1DMqVApQioqmkODWMh4ADEnMFeYbYy/O64nQ3Adp0XKUKibzMgxWDFCEqibNYUEG11jRficANPcpiGscwAsAFwGAUITFUrUCmoFKEVEataGtnndMDQ25x67tQcsiwaEIRUltlYEN1XllpdnqiQ0WElaVQhCYOTek2pLBOrZyQG9YHK+ouWdQaEIRUVWYUmPDhtLnuAA0heO4U4aypMrGDm5p6vFCFyZRayWjsPazZk8JRxHrqkcGJELjMrNCFws97UCEIQAIQhAAm6DQzEdg0XnwQhXZxUpUZlbzcLNyR0qfT4bIeSg2mUi4c0DPI5zp0rhkoQlKbm6sLGyVnHR16yEIQpNQW0F4HOExosI1IQitNImq6B+jwWA5QcqVwuFbNWGZI0psnX1jeTpKELSXypnPZ1vyr1fsYIQhZnSf/9k=',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
    ],
  }),
  watch: {
    isOpen(newVal) {
      this.isModalOpen = newVal
    },
    isModalOpen(newVal) {
      if (!newVal) {
        this.onModalHide()
      }
    },
  },
  mounted() {},
  methods: {
    closeShowImgModal() {
      this.isShowImgModal = false
    },
    showModalImg(index, srcImg) {
      // // Get the modal
      // let modal = document.getElementById(`ImgModal${index}`)

      // // Get the image and insert it inside the modal - use its "alt" text as a caption
      // // let img = document.getElementById(`ImgModal${index}`)
      // let modalImg = document.getElementById(`modalImg${index}`)

      // modal.style.display = 'block'
      // modalImg.src = srcImg
      this.isShowImgModal = true
      this.imgDataModal.src = srcImg
    },
    closeModalImg(index) {
      // let span = document.getElementsByClassName("close-img-modal")[0];
      let modal = document.getElementById(`ImgModal${index}`)

      // When the user clicks on <span> (x), close the modal

      modal.style.display = 'none'
    },
    setShowmore() {
      if (this.showMore === true) {
        this.showMore = false
      } else {
        this.showMore = true
      }
    },
    onModalHide() {
      this.$emit('onModalHide', false)
    },
    formatAge(value) {
      let d = new Date(value)
      let n = d.getFullYear()
      n = new Date().getFullYear() - n
      if (n < 11) {
        return `0 - 10 ปี`
      } else if (10 < n < 21) {
        return `11 - 20 ปี`
      } else if (20 < n < 31) {
        return `21 - 30 ปี`
      } else if (30 < n < 41) {
        return `31 - 40 ปี`
      } else if (40 < n < 51) {
        return `41 - 50 ปี`
      } else if (50 < n < 61) {
        return `51 - 60 ปี`
      } else if (60 < n < 71) {
        return `61 - 70 ปี`
      } else if (70 < n < 81) {
        return `71 - 80 ปี`
      } else {
        return ` > 80 ปี`
      }
    },
  },
}
</script>

<style lang="scss">
.sectionImg {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  height: 180px;
  overflow: hidden;
}
.sectionImg > div {
  width: 100%;
}
.activeShowMore {
  height: 100% !important;
  overflow: initial;
}
/* The Modal (background) */
.userImgModal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  vertical-align: middle;
  padding-top: 10%; /* Location of the box */
  left: 0;
  top: 0;
  margin: 0 auto;
  width: 100vw; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.9); /* Black w/ opacity */
}
/* Modal Content (image) */
.img-modal-content {
  margin: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 80%;
  max-width: 100%;
}
/* Add Animation */
.img-modal-content {
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.6s;
  animation-name: zoom;
  animation-duration: 0.6s;
}

@-webkit-keyframes zoom {
  from {
    -webkit-transform: scale(0);
  }
  to {
    -webkit-transform: scale(1);
  }
}

@keyframes zoom {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

/* The Close Button */
.close-img-modal {
  position: absolute;
  top: 25px;
  right: 35px;
  color: #f1f1f1;
  font-size: 30px;
  transition: 0.3s;
}

.close-img-modal:hover,
.close-img-modal:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}

/* 100% Image Width on Smaller Screens */
@media only screen and (max-width: 700px) {
  .img-modal-content {
    width: 100%;
  }
  .sectionImg {
    grid-template-columns: repeat(2, 1fr);
    height: 145px;
  }
}
.img-thumbnail {
  background-color: #f5f5f5;
  box-shadow: none;
  border: 0px solid;
  border-radius: -22.8125rem;
  max-width: 100%;
  height: auto;
  cursor: pointer;
}
.img-thumbnail:hover {
  opacity: 0.8;
}
.txt_patientInfo_16px {
  color: #333333;
  font-size: 16px;
  padding-bottom: 0.5rem;
}
.txt_patientInfo_16px span {
  color: #707683;
}
.txt_patientInfo_13px {
  color: #707683;
  font-size: 13px;
  padding: 0.5em 0;
}
.patient-info-modal {
  .modal-header {
    width: 100%;
    margin: 0 !important;
  }

  .modal-body {
    padding: 8px 0;
    overflow-y: auto;

    .btn {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
}
</style>
