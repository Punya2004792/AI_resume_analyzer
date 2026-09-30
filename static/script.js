document.addEventListener(
    "DOMContentLoaded",
    function () {

        initializeProgressBars();

        initializeAnalytics();

        initializeKeywordBar();

        initializeUploadInteractions();

        initializeFormLoading();

    }
);


function initializeProgressBars() {

    const progressBars =
        document.querySelectorAll(
            ".progress-fill"
        );


    progressBars.forEach(
        function (bar, index) {

            let score =
                parseFloat(
                    bar.dataset.score
                );


            if (isNaN(score)) {
                score = 0;
            }


            score =
                Math.max(
                    0,
                    Math.min(score, 100)
                );


            setTimeout(
                function () {

                    bar.style.width =
                        score + "%";

                },
                150 + index * 100
            );

        }
    );
}


function initializeAnalytics() {

    const metricBars =
        document.querySelectorAll(
            ".metric-bar"
        );


    metricBars.forEach(
        function (bar, index) {

            let value =
                parseFloat(
                    bar.dataset.value
                );


            if (isNaN(value)) {
                value = 0;
            }


            value =
                Math.max(
                    0,
                    Math.min(value, 100)
                );


            setTimeout(
                function () {

                    bar.style.width =
                        value + "%";

                },
                300 + index * 120
            );

        }
    );
}


function initializeKeywordBar() {

    const keywordBar =
        document.querySelector(
            ".keyword-progress-fill"
        );


    if (!keywordBar) {
        return;
    }


    let value =
        parseFloat(
            keywordBar.dataset.value
        );


    if (isNaN(value)) {
        value = 0;
    }


    value =
        Math.max(
            0,
            Math.min(value, 100)
        );


    setTimeout(
        function () {

            keywordBar.style.width =
                value + "%";

        },
        500
    );
}


function initializeUploadInteractions() {

    const fileInput =
        document.querySelector(
            "#resume"
        );


    const fileNameDisplay =
        document.querySelector(
            "#file-name"
        );


    if (!fileInput) {
        return;
    }


    fileInput.addEventListener(
        "change",
        function () {

            if (
                this.files &&
                this.files.length > 0
            ) {

                const file =
                    this.files[0];


                if (fileNameDisplay) {

                    fileNameDisplay.textContent =
                        file.name;

                }

            }

        }
    );
}


function initializeFormLoading() {

    const form =
        document.querySelector(
            "form"
        );


    if (!form) {
        return;
    }


    form.addEventListener(
        "submit",
        function () {

            const button =
                form.querySelector(
                    "button[type='submit']"
                );


            if (button) {

                button.disabled =
                    true;

                button.textContent =
                    "Analyzing...";

            }

        }
    );
}