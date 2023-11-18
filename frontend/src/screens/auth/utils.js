import * as yup from 'yup';

export const loginInitialValue = {
    username: '',
    password: ''
};

export const loginValidationSchema = yup.object().shape({
    username: yup.string().required('username is required'),
    password: yup.string().required('password is required'),
})

export const SignupInitialValue = {
    firstName: '',
    lastName: '',
    DOB: '',
    Gender:'',
    country:'',
    number : '',
};

export const SignupValidationSchema = yup.object().shape({
    number: yup.string().min(
        10,({min}) => 
        `${'Mobile number must be'} ${min} ${'character'}`,
    )
    .required('Mobile number is required')
    .matches(/^[789]\d{9}$/,'Mobile number should be start from 7,8,9'),
    firstName: yup.string().required('FirstName is required'),
    lastName: yup.string().required('LastName is required'),
    DOB: yup.string().required('Date of Birth is required'),
    Gender: yup.string().required('Gender is required'),
    country: yup.string().required('Country is required')
});
