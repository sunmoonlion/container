const { createApp, ref } = Vue;

const app = createApp({
    setup() {
        // Reactive state
        const username = ref('');
        const email = ref('');
        const password = ref('');
        const password2 = ref('');
        const mobile = ref('');
        const allow = ref(false);

        // Validation states
        const error_name = ref(false);
        const error_email = ref(false);
        const error_password = ref(false);
        const error_password2 = ref(false);
        const error_mobile = ref(false);
        const error_allow = ref(false);

        // Error messages
        const error_name_message = ref('');
        const error_email_message = ref('');
        const error_password_message = ref('');
        const error_password2_message = ref('');
        const error_mobile_message = ref('');
        const error_allow_message = ref('');

        // Methods
        const check_username = () => {
            // Validation logic for username
            // Update error_name and error_name_message accordingly
        };

        const check_email = () => {
            // Validation logic for email
            // Update error_email and error_email_message accordingly
        };

        const check_password = () => {
            // Validation logic for password
            // Update error_password and error_password_message accordingly
        };

        const check_password2 = () => {
            // Validation logic for confirm password
            // Update error_password2 and error_password2_message accordingly
        };

        const check_mobile = () => {
            // Validation logic for mobile number
            // Update error_mobile and error_mobile_message accordingly
        };

        const check_allow = () => {
            // Validation logic for terms agreement
            // Update error_allow and error_allow_message accordingly
        };

        const on_submit = () => {
            // Perform all validations
            check_username();
            check_email();
            check_password();
            check_password2();
            check_mobile();
            check_allow();

            // If there are any errors, prevent form submission
            if (error_name.value || error_email.value || error_password.value || error_password2.value || error_mobile.value || error_allow.value) {
                return;
            }

            // Otherwise, submit the form or perform additional logic
            // Example: make HTTP request to register user
            // axios.post('/register', { username.value, email.value, password.value, mobile.value })
            //     .then(response => {
            //         // Handle success
            //     })
            //     .catch(error => {
            //         // Handle error
            //     });
        };

        // Return reactive data and methods
        return {
            username,
            email,
            password,
            password2,
            mobile,
            allow,
            error_name,
            error_email,
            error_password,
            error_password2,
            error_mobile,
            error_allow,
            error_name_message,
            error_email_message,
            error_password_message,
            error_password2_message,
            error_mobile_message,
            error_allow_message,
            on_submit,
        };
    },
});

app.config.compilerOptions.delimiters = ['[[', ']]'];

app.mount('#app');
