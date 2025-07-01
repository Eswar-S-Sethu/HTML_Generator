let wasm;

/**
 * @param {number} lbs
 * @returns {number}
 */
export function lbs_to_kg(lbs) {
    const ret = wasm.lbs_to_kg(lbs);
    return ret;
}

/**
 * @param {number} kg
 * @returns {number}
 */
export function kg_to_lbs(kg) {
    const ret = wasm.kg_to_lbs(kg);
    return ret;
}

/**
 * @param {number} cm
 * @returns {number}
 */
export function cm_to_in(cm) {
    const ret = wasm.cm_to_in(cm);
    return ret;
}

/**
 * @param {number} inches
 * @returns {number}
 */
export function in_to_cm(inches) {
    const ret = wasm.in_to_cm(inches);
    return ret;
}

/**
 * @param {number} m
 * @returns {number}
 */
export function m_to_km(m) {
    const ret = wasm.m_to_km(m);
    return ret;
}

/**
 * @param {number} km
 * @returns {number}
 */
export function km_to_m(km) {
    const ret = wasm.km_to_m(km);
    return ret;
}

/**
 * @param {number} c
 * @returns {number}
 */
export function c_to_f(c) {
    const ret = wasm.c_to_f(c);
    return ret;
}

/**
 * @param {number} f
 * @returns {number}
 */
export function f_to_c(f) {
    const ret = wasm.f_to_c(f);
    return ret;
}

/**
 * @param {number} c
 * @returns {number}
 */
export function c_to_k(c) {
    const ret = wasm.c_to_k(c);
    return ret;
}

/**
 * @param {number} k
 * @returns {number}
 */
export function k_to_c(k) {
    const ret = wasm.k_to_c(k);
    return ret;
}

/**
 * @param {number} kmh
 * @returns {number}
 */
export function kmh_to_mph(kmh) {
    const ret = wasm.kmh_to_mph(kmh);
    return ret;
}

/**
 * @param {number} mph
 * @returns {number}
 */
export function mph_to_kmh(mph) {
    const ret = wasm.mph_to_kmh(mph);
    return ret;
}

/**
 * @param {number} sqm
 * @returns {number}
 */
export function sqm_to_sqft(sqm) {
    const ret = wasm.sqm_to_sqft(sqm);
    return ret;
}

/**
 * @param {number} sqft
 * @returns {number}
 */
export function sqft_to_sqm(sqft) {
    const ret = wasm.sqft_to_sqm(sqft);
    return ret;
}

/**
 * @param {number} l
 * @returns {number}
 */
export function l_to_gal(l) {
    const ret = wasm.l_to_gal(l);
    return ret;
}

/**
 * @param {number} gal
 * @returns {number}
 */
export function gal_to_l(gal) {
    const ret = wasm.gal_to_l(gal);
    return ret;
}

/**
 * @param {number} hrs
 * @returns {number}
 */
export function hrs_to_min(hrs) {
    const ret = wasm.hrs_to_min(hrs);
    return ret;
}

/**
 * @param {number} min
 * @returns {number}
 */
export function min_to_sec(min) {
    const ret = wasm.hrs_to_min(min);
    return ret;
}

/**
 * @param {number} pa
 * @returns {number}
 */
export function pa_to_psi(pa) {
    const ret = wasm.pa_to_psi(pa);
    return ret;
}

/**
 * @param {number} psi
 * @returns {number}
 */
export function psi_to_pa(psi) {
    const ret = wasm.psi_to_pa(psi);
    return ret;
}

/**
 * @param {number} j
 * @returns {number}
 */
export function j_to_cal(j) {
    const ret = wasm.j_to_cal(j);
    return ret;
}

/**
 * @param {number} cal
 * @returns {number}
 */
export function cal_to_j(cal) {
    const ret = wasm.cal_to_j(cal);
    return ret;
}

/**
 * @param {number} w
 * @returns {number}
 */
export function w_to_kw(w) {
    const ret = wasm.m_to_km(w);
    return ret;
}

/**
 * @param {number} kw
 * @returns {number}
 */
export function kw_to_w(kw) {
    const ret = wasm.km_to_m(kw);
    return ret;
}

/**
 * @param {number} kb
 * @returns {number}
 */
export function kb_to_mb(kb) {
    const ret = wasm.gb_to_tb(kb);
    return ret;
}

/**
 * @param {number} mb
 * @returns {number}
 */
export function mb_to_gb(mb) {
    const ret = wasm.gb_to_tb(mb);
    return ret;
}

/**
 * @param {number} gb
 * @returns {number}
 */
export function gb_to_tb(gb) {
    const ret = wasm.gb_to_tb(gb);
    return ret;
}

/**
 * @param {number} us_size
 * @returns {number}
 */
export function us_to_eu_ring(us_size) {
    const ret = wasm.us_to_eu_ring(us_size);
    return ret;
}

/**
 * @param {number} eu_size
 * @returns {number}
 */
export function eu_to_us_ring(eu_size) {
    const ret = wasm.eu_to_us_ring(eu_size);
    return ret;
}

/**
 * @param {number} us_size
 * @returns {number}
 */
export function us_shoe_to_eu(us_size) {
    const ret = wasm.us_shoe_to_eu(us_size);
    return ret;
}

/**
 * @param {number} eu_size
 * @returns {number}
 */
export function eu_shoe_to_us(eu_size) {
    const ret = wasm.eu_shoe_to_us(eu_size);
    return ret;
}

/**
 * @param {number} us_size
 * @returns {number}
 */
export function us_to_eu_clothing(us_size) {
    const ret = wasm.us_to_eu_clothing(us_size);
    return ret;
}

/**
 * @param {number} eu_size
 * @returns {number}
 */
export function eu_to_us_clothing(eu_size) {
    const ret = wasm.eu_to_us_clothing(eu_size);
    return ret;
}

/**
 * @param {number} tsp
 * @returns {number}
 */
export function tsp_to_tbsp(tsp) {
    const ret = wasm.tsp_to_tbsp(tsp);
    return ret;
}

/**
 * @param {number} tbsp
 * @returns {number}
 */
export function tbsp_to_tsp(tbsp) {
    const ret = wasm.tbsp_to_tsp(tbsp);
    return ret;
}

/**
 * @param {number} cup
 * @returns {number}
 */
export function cup_to_ml(cup) {
    const ret = wasm.cup_to_ml(cup);
    return ret;
}

/**
 * @param {number} ml
 * @returns {number}
 */
export function ml_to_cup(ml) {
    const ret = wasm.ml_to_cup(ml);
    return ret;
}

/**
 * @param {number} oz
 * @returns {number}
 */
export function oz_to_grams(oz) {
    const ret = wasm.oz_to_grams(oz);
    return ret;
}

/**
 * @param {number} g
 * @returns {number}
 */
export function grams_to_oz(g) {
    const ret = wasm.grams_to_oz(g);
    return ret;
}

/**
 * @param {number} steps
 * @returns {number}
 */
export function steps_to_km(steps) {
    const ret = wasm.steps_to_km(steps);
    return ret;
}

/**
 * @param {number} km
 * @returns {number}
 */
export function km_to_steps(km) {
    const ret = wasm.km_to_steps(km);
    return ret;
}

/**
 * @param {number} n
 * @returns {number}
 */
export function newtons_to_pounds_force(n) {
    const ret = wasm.newtons_to_pounds_force(n);
    return ret;
}

/**
 * @param {number} lbf
 * @returns {number}
 */
export function pounds_force_to_newtons(lbf) {
    const ret = wasm.pounds_force_to_newtons(lbf);
    return ret;
}

/**
 * @param {number} wpm
 * @returns {number}
 */
export function wpm_to_cpm(wpm) {
    const ret = wasm.wpm_to_cpm(wpm);
    return ret;
}

/**
 * @param {number} cpm
 * @returns {number}
 */
export function cpm_to_wpm(cpm) {
    const ret = wasm.cpm_to_wpm(cpm);
    return ret;
}

/**
 * @param {number} percent
 * @returns {number}
 */
export function percent_to_gpa(percent) {
    const ret = wasm.percent_to_gpa(percent);
    return ret;
}

/**
 * @param {number} gpa
 * @returns {number}
 */
export function gpa_to_percent(gpa) {
    const ret = wasm.gpa_to_percent(gpa);
    return ret;
}

let WASM_VECTOR_LEN = 0;

let cachedUint8ArrayMemory0 = null;

function getUint8ArrayMemory0() {
    if (cachedUint8ArrayMemory0 === null || cachedUint8ArrayMemory0.byteLength === 0) {
        cachedUint8ArrayMemory0 = new Uint8Array(wasm.memory.buffer);
    }
    return cachedUint8ArrayMemory0;
}

const cachedTextEncoder = (typeof TextEncoder !== 'undefined' ? new TextEncoder('utf-8') : { encode: () => { throw Error('TextEncoder not available') } } );

const encodeString = (typeof cachedTextEncoder.encodeInto === 'function'
    ? function (arg, view) {
    return cachedTextEncoder.encodeInto(arg, view);
}
    : function (arg, view) {
    const buf = cachedTextEncoder.encode(arg);
    view.set(buf);
    return {
        read: arg.length,
        written: buf.length
    };
});

function passStringToWasm0(arg, malloc, realloc) {

    if (realloc === undefined) {
        const buf = cachedTextEncoder.encode(arg);
        const ptr = malloc(buf.length, 1) >>> 0;
        getUint8ArrayMemory0().subarray(ptr, ptr + buf.length).set(buf);
        WASM_VECTOR_LEN = buf.length;
        return ptr;
    }

    let len = arg.length;
    let ptr = malloc(len, 1) >>> 0;

    const mem = getUint8ArrayMemory0();

    let offset = 0;

    for (; offset < len; offset++) {
        const code = arg.charCodeAt(offset);
        if (code > 0x7F) break;
        mem[ptr + offset] = code;
    }

    if (offset !== len) {
        if (offset !== 0) {
            arg = arg.slice(offset);
        }
        ptr = realloc(ptr, len, len = offset + arg.length * 3, 1) >>> 0;
        const view = getUint8ArrayMemory0().subarray(ptr + offset, ptr + len);
        const ret = encodeString(arg, view);

        offset += ret.written;
        ptr = realloc(ptr, len, offset, 1) >>> 0;
    }

    WASM_VECTOR_LEN = offset;
    return ptr;
}

const cachedTextDecoder = (typeof TextDecoder !== 'undefined' ? new TextDecoder('utf-8', { ignoreBOM: true, fatal: true }) : { decode: () => { throw Error('TextDecoder not available') } } );

if (typeof TextDecoder !== 'undefined') { cachedTextDecoder.decode(); };

function getStringFromWasm0(ptr, len) {
    ptr = ptr >>> 0;
    return cachedTextDecoder.decode(getUint8ArrayMemory0().subarray(ptr, ptr + len));
}
/**
 * @param {string} data_json
 * @param {string} from_unit
 * @param {string} to_unit
 * @returns {string}
 */
export function convert_columns(data_json, from_unit, to_unit) {
    let deferred4_0;
    let deferred4_1;
    try {
        const ptr0 = passStringToWasm0(data_json, wasm.__wbindgen_malloc, wasm.__wbindgen_realloc);
        const len0 = WASM_VECTOR_LEN;
        const ptr1 = passStringToWasm0(from_unit, wasm.__wbindgen_malloc, wasm.__wbindgen_realloc);
        const len1 = WASM_VECTOR_LEN;
        const ptr2 = passStringToWasm0(to_unit, wasm.__wbindgen_malloc, wasm.__wbindgen_realloc);
        const len2 = WASM_VECTOR_LEN;
        const ret = wasm.convert_columns(ptr0, len0, ptr1, len1, ptr2, len2);
        deferred4_0 = ret[0];
        deferred4_1 = ret[1];
        return getStringFromWasm0(ret[0], ret[1]);
    } finally {
        wasm.__wbindgen_free(deferred4_0, deferred4_1, 1);
    }
}

async function __wbg_load(module, imports) {
    if (typeof Response === 'function' && module instanceof Response) {
        if (typeof WebAssembly.instantiateStreaming === 'function') {
            try {
                return await WebAssembly.instantiateStreaming(module, imports);

            } catch (e) {
                if (module.headers.get('Content-Type') != 'application/wasm') {
                    console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve Wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n", e);

                } else {
                    throw e;
                }
            }
        }

        const bytes = await module.arrayBuffer();
        return await WebAssembly.instantiate(bytes, imports);

    } else {
        const instance = await WebAssembly.instantiate(module, imports);

        if (instance instanceof WebAssembly.Instance) {
            return { instance, module };

        } else {
            return instance;
        }
    }
}

function __wbg_get_imports() {
    const imports = {};
    imports.wbg = {};
    imports.wbg.__wbindgen_init_externref_table = function() {
        const table = wasm.__wbindgen_export_0;
        const offset = table.grow(4);
        table.set(0, undefined);
        table.set(offset + 0, undefined);
        table.set(offset + 1, null);
        table.set(offset + 2, true);
        table.set(offset + 3, false);
        ;
    };

    return imports;
}

function __wbg_init_memory(imports, memory) {

}

function __wbg_finalize_init(instance, module) {
    wasm = instance.exports;
    __wbg_init.__wbindgen_wasm_module = module;
    cachedUint8ArrayMemory0 = null;


    wasm.__wbindgen_start();
    return wasm;
}

function initSync(module) {
    if (wasm !== undefined) return wasm;


    if (typeof module !== 'undefined') {
        if (Object.getPrototypeOf(module) === Object.prototype) {
            ({module} = module)
        } else {
            console.warn('using deprecated parameters for `initSync()`; pass a single object instead')
        }
    }

    const imports = __wbg_get_imports();

    __wbg_init_memory(imports);

    if (!(module instanceof WebAssembly.Module)) {
        module = new WebAssembly.Module(module);
    }

    const instance = new WebAssembly.Instance(module, imports);

    return __wbg_finalize_init(instance, module);
}

async function __wbg_init(module_or_path) {
    if (wasm !== undefined) return wasm;


    if (typeof module_or_path !== 'undefined') {
        if (Object.getPrototypeOf(module_or_path) === Object.prototype) {
            ({module_or_path} = module_or_path)
        } else {
            console.warn('using deprecated parameters for the initialization function; pass a single object instead')
        }
    }

    if (typeof module_or_path === 'undefined') {
        module_or_path = new URL('UnitConverter_bg.wasm', import.meta.url);
    }
    const imports = __wbg_get_imports();

    if (typeof module_or_path === 'string' || (typeof Request === 'function' && module_or_path instanceof Request) || (typeof URL === 'function' && module_or_path instanceof URL)) {
        module_or_path = fetch(module_or_path);
    }

    __wbg_init_memory(imports);

    const { instance, module } = await __wbg_load(await module_or_path, imports);

    return __wbg_finalize_init(instance, module);
}

export { initSync };
export default __wbg_init;
