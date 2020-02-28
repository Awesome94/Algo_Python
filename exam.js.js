const exams = function (v) {
    let numOfQtns = 0;
    const n = v.length;

    for (x = 0; x < n; x++) {
        if (v[x] == 0) {
            v[x] = -1
        };
    };
    for (x = 0; x < n; x++) {
        if (eval(v.slice(0, x).join('+')) > eval(v.slice(x, n).join('+'))) {
            return numOfQtns;
        } else {
            numOfQtns++
        }
    }
}

const arr = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1,
    1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
console.log(exams(arr))



