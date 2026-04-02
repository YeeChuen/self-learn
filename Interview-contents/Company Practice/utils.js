export function ValidityState(log, actual, expectation) {
    const result = actual === expectation ? "PASSED" : "FAILED";
    message = `Result :${result}, actual: ${actual}, expected: ${expectation} [${log}]`;
    console.log(message);
}