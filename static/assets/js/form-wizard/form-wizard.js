 // Initial setup
 let currentTab = 0; // Current tab is set to be the first tab (0)
 showTab(currentTab); // Display the current tab

 function showTab(n) {
     const tabs = document.querySelectorAll(".tab");
     tabs[n].style.display = "block"; // Display the current tab
     // Fix the Previous/Next buttons
     if (n === 0) {
         document.getElementById("prevBtn").style.display = "none";
     } else {
         document.getElementById("prevBtn").style.display = "inline";
     }
     if (n === (tabs.length - 1)) {
         document.getElementById("nextBtn").innerHTML = "Submit"; // Change next button to "Submit"
     } else {
         document.getElementById("nextBtn").innerHTML = "Next";
     }
     // Update the step indicators
     updateStepIndicator(n);
 }

 function nextPrev(n) {
    const tabs = document.querySelectorAll(".tab");

    // Validate the current tab before moving forward
    if (n === 1 && !validateForm()) {
        console.log(`Validation failed on step: ${currentTab}`);
        return false; // Stop if the form is invalid
    }

    // Hide the current tab
    tabs[currentTab].style.display = "none";
    
    // Increase or decrease the current tab by n (Previous or Next)
    currentTab += n;

    // If you've reached the end of the form
    if (currentTab >= tabs.length) {
        document.getElementById("regForm").submit();
        return false;
    }

    // Otherwise, show the correct tab
    showTab(currentTab);
}
function validateForm() {
    const tabs = document.querySelectorAll(".tab");
    const inputs = tabs[currentTab].querySelectorAll("input, select, textarea");
    let valid = true;

    inputs.forEach(input => {
        const feedback = input.nextElementSibling; // Assuming .invalid-feedback comes right after the input

        if (input.hasAttribute('required') && input.value.trim() === "") {
            input.classList.add("is-invalid"); // Add invalid class to highlight the input
            if (feedback && feedback.classList.contains("invalid-feedback")) {
                feedback.style.display = "block"; // Show the invalid-feedback message
            }
            valid = false;
        } else {
            input.classList.remove("is-invalid"); // Remove the invalid class if input is valid
            if (feedback && feedback.classList.contains("invalid-feedback")) {
                feedback.style.display = "none"; // Hide the invalid-feedback message if valid
            }
        }
    });

    return valid; // Return true if all fields are valid, false otherwise
}
