import * as Yup from 'yup'

const passwordShape = Yup.string()
  .required('validation.password.required')
  .matches(
    /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/,
    'validation.password.invalid'
  )

export { passwordShape }
