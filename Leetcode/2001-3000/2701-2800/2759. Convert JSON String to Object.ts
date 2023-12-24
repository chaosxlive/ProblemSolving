// https://leetcode.com/problems/convert-json-string-to-object/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function jsonParse(s: string): JSONValue {
    if (s[0] === '{') {
        return parseJsonObject(s);
    } else if (s[0] === '[') {
        return parseJsonArray(s);
    } else if (s[0] === '"') {
        return s.substring(1, s.length - 1);
    } else if (s[0] === 't') {
        return true;
    } else if (s[0] === 'f') {
        return false;
    } else if (s[0] === 'n') {
        return null;
    } else {
        return +s;
    }
};

function parseJsonObject(s: string): { [key: string]: JSONValue } {
    const result: { [key: string]: JSONValue } = {};
    let i = 2;
    let keyStartIdx = 2;
    while (i < s.length) {
        while (s[i] !== '"') {
            i++;
        }
        const key = s.substring(keyStartIdx, i);
        i += 2
        const valueStartIdx = i;
        let bracketCnt = 0;
        let isQuote = false;
        while (true) {
            if (s[i] === '{') {
                bracketCnt++;
            } else if (s[i] === '[') {
                bracketCnt++;
            } else if (s[i] === ']') {
                bracketCnt--;
            } else if (s[i] === '"') {
                isQuote = !isQuote;
            } else if (s[i] === '}') {
                if (bracketCnt === 0 && !isQuote) {
                    break;
                }
                bracketCnt--;
            } else if (s[i] === ',') {
                if (bracketCnt === 0 && !isQuote) {
                    break;
                }
            }
            i++;
        }
        const value = s.substring(valueStartIdx, i);
        result[key] = jsonParse(value);
        keyStartIdx = i + 2;
        i += 2;
    }
    return result;
}

function parseJsonArray(s: string): JSONValue[] {
    const result: JSONValue[] = [];
    if (s === '[]') {
        return result;
    }
    let i = 1;
    let valueStartIdx = 1;
    while (i < s.length) {
        let bracketCnt = 0;
        let isQuote = false;
        while (true) {
            if (s[i] === '[') {
                bracketCnt++;
            } else if (s[i] === '{') {
                bracketCnt++;
            } else if (s[i] === '}') {
                bracketCnt--;
            } else if (s[i] === '"') {
                isQuote = !isQuote;
            } else if (s[i] === ']' && !isQuote) {
                if (bracketCnt === 0) {
                    break;
                }
                bracketCnt--;
            } else if (s[i] === ',') {
                if (bracketCnt === 0 && !isQuote) {
                    break;
                }
            }
            i++;
        }
        const value = s.substring(valueStartIdx, i);
        result.push(jsonParse(value));
        valueStartIdx = i + 1;
        i += 1;
    }
    return result;
}
