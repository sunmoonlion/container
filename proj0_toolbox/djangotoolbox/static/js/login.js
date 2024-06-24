const { createApp, ref, onMounted } = Vue;

const app = createApp({
    setup() {
        // Reactive state
        const username = ref('');
        const password = ref(''); 
        const remembered = ref('false');

        // Validation states
        const error_name = ref(false);
        const error_password = ref(false);       

        // Methods

        const check_username = () => {
            let re = /^[a-zA-Z0-9_-]{5,20}$/;
			if (re.test(this.username)) {
                this.error_username = false;
            } else {
                this.error_username = true;
            }
        };

        const check_password = () => {
            const re = /^[0-9A-Za-z]{8,20}$/;
            if (re.test(password.value)) {
                error_password.value = false;
            } else {
                error_password.value = true;
            }
        };

        const on_submit = (event) => {
            check_username();
            check_password();

            if (error_name.value || error_password.value ) { 
                event.preventDefault();
            }
        };

        return {
            username,
            password,
            remembered,
            error_name,
            error_password,
            check_username,
            check_password,
            on_submit
        };
    }
});

app.config.compilerOptions.delimiters = ['[[', ']]'];

app.mount('#app');
