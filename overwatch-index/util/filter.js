/* eslint-disable */
const filterByPredicate = function (obj, predicate) {
    let result = {}, key;

    for (key in obj) {
        if (obj.hasOwnProperty(key) && predicate(obj[key])) {
            result[key] = obj[key];
        }
    }

    return result;
};
/* eslint-enable */

export default filterByPredicate;