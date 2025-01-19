// function countUp(elementId, targetValue, duration, label) {
//     const element = document.getElementById(elementId);
//     let current = 0;
//     const increment = Math.ceil(targetValue / (duration / 50)); // Adjust speed
//     const interval = setInterval(() => {
//       current += increment;
//       if (current >= targetValue) {
//         current = targetValue;
//         clearInterval(interval);
//       }
//       element.textContent = `${label} - ${current}`;
//     }, 50); // Interval in milliseconds
//   }
  
//   // Start counting effect
//   document.addEventListener("DOMContentLoaded", () => {
//     countUp("projectCount", 200, 2000, "Projects"); // Count to 200 over 2 seconds
//     countUp("certificationCount", 185, 2000, "Certifications"); // Count to 185 over 2 seconds
//   });

// counting.js
// function countUp(elementId, target, duration) {
//   const element = document.getElementById(elementId);
//   let start = 0;
//   const stepTime = Math.abs(Math.floor(duration / target));
//   function updateCount() {
//       start++;
//       element.textContent = start;
//       if (start < target) {
//           setTimeout(updateCount, stepTime);
//       }
//   }
//   updateCount();
// }

// function startCounting() {
//   countUp("projectCount", 200, 2000, "Projects"); // Projects count
//   countUp("certificationCount", 185, 2000, "Certifications"); // Certifications count
// }


function countUp(elementId, label, target, duration) {
  const element = document.getElementById(elementId);
  let start = 0;
  const stepTime = Math.abs(Math.floor(duration / target));

  function updateCount() {
      start++;
      element.textContent = `${label} - ${start}`;
      if (start < target) {
          setTimeout(updateCount, stepTime);
      }
  }

  updateCount();
}

function startCounting() {
  countUp("projectCount", "Projects", 200, 2000); // Projects count
  countUp("certificationCount", "Certifications", 185, 2000); // Certifications count
}
