/* tslint:disable */
/* eslint-disable */
export function lbs_to_kg(lbs: number): number;
export function kg_to_lbs(kg: number): number;
export function cm_to_in(cm: number): number;
export function in_to_cm(inches: number): number;
export function m_to_km(m: number): number;
export function km_to_m(km: number): number;
export function c_to_f(c: number): number;
export function f_to_c(f: number): number;
export function c_to_k(c: number): number;
export function k_to_c(k: number): number;
export function kmh_to_mph(kmh: number): number;
export function mph_to_kmh(mph: number): number;
export function sqm_to_sqft(sqm: number): number;
export function sqft_to_sqm(sqft: number): number;
export function l_to_gal(l: number): number;
export function gal_to_l(gal: number): number;
export function hrs_to_min(hrs: number): number;
export function min_to_sec(min: number): number;
export function pa_to_psi(pa: number): number;
export function psi_to_pa(psi: number): number;
export function j_to_cal(j: number): number;
export function cal_to_j(cal: number): number;
export function w_to_kw(w: number): number;
export function kw_to_w(kw: number): number;
export function kb_to_mb(kb: number): number;
export function mb_to_gb(mb: number): number;
export function gb_to_tb(gb: number): number;
export function us_to_eu_ring(us_size: number): number;
export function eu_to_us_ring(eu_size: number): number;
export function us_shoe_to_eu(us_size: number): number;
export function eu_shoe_to_us(eu_size: number): number;
export function us_to_eu_clothing(us_size: number): number;
export function eu_to_us_clothing(eu_size: number): number;
export function tsp_to_tbsp(tsp: number): number;
export function tbsp_to_tsp(tbsp: number): number;
export function cup_to_ml(cup: number): number;
export function ml_to_cup(ml: number): number;
export function oz_to_grams(oz: number): number;
export function grams_to_oz(g: number): number;
export function steps_to_km(steps: number): number;
export function km_to_steps(km: number): number;
export function newtons_to_pounds_force(n: number): number;
export function pounds_force_to_newtons(lbf: number): number;
export function wpm_to_cpm(wpm: number): number;
export function cpm_to_wpm(cpm: number): number;
export function percent_to_gpa(percent: number): number;
export function gpa_to_percent(gpa: number): number;
export function convert_columns(data_json: string, from_unit: string, to_unit: string): string;

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly lbs_to_kg: (a: number) => number;
  readonly kg_to_lbs: (a: number) => number;
  readonly cm_to_in: (a: number) => number;
  readonly in_to_cm: (a: number) => number;
  readonly m_to_km: (a: number) => number;
  readonly km_to_m: (a: number) => number;
  readonly c_to_f: (a: number) => number;
  readonly f_to_c: (a: number) => number;
  readonly c_to_k: (a: number) => number;
  readonly k_to_c: (a: number) => number;
  readonly kmh_to_mph: (a: number) => number;
  readonly mph_to_kmh: (a: number) => number;
  readonly sqm_to_sqft: (a: number) => number;
  readonly sqft_to_sqm: (a: number) => number;
  readonly l_to_gal: (a: number) => number;
  readonly gal_to_l: (a: number) => number;
  readonly hrs_to_min: (a: number) => number;
  readonly pa_to_psi: (a: number) => number;
  readonly psi_to_pa: (a: number) => number;
  readonly j_to_cal: (a: number) => number;
  readonly cal_to_j: (a: number) => number;
  readonly gb_to_tb: (a: number) => number;
  readonly us_to_eu_ring: (a: number) => number;
  readonly eu_to_us_ring: (a: number) => number;
  readonly us_shoe_to_eu: (a: number) => number;
  readonly eu_shoe_to_us: (a: number) => number;
  readonly us_to_eu_clothing: (a: number) => number;
  readonly eu_to_us_clothing: (a: number) => number;
  readonly tsp_to_tbsp: (a: number) => number;
  readonly tbsp_to_tsp: (a: number) => number;
  readonly cup_to_ml: (a: number) => number;
  readonly ml_to_cup: (a: number) => number;
  readonly oz_to_grams: (a: number) => number;
  readonly grams_to_oz: (a: number) => number;
  readonly steps_to_km: (a: number) => number;
  readonly km_to_steps: (a: number) => number;
  readonly newtons_to_pounds_force: (a: number) => number;
  readonly pounds_force_to_newtons: (a: number) => number;
  readonly wpm_to_cpm: (a: number) => number;
  readonly cpm_to_wpm: (a: number) => number;
  readonly percent_to_gpa: (a: number) => number;
  readonly gpa_to_percent: (a: number) => number;
  readonly convert_columns: (a: number, b: number, c: number, d: number, e: number, f: number) => [number, number];
  readonly w_to_kw: (a: number) => number;
  readonly min_to_sec: (a: number) => number;
  readonly kw_to_w: (a: number) => number;
  readonly mb_to_gb: (a: number) => number;
  readonly kb_to_mb: (a: number) => number;
  readonly __wbindgen_export_0: WebAssembly.Table;
  readonly __wbindgen_malloc: (a: number, b: number) => number;
  readonly __wbindgen_realloc: (a: number, b: number, c: number, d: number) => number;
  readonly __wbindgen_free: (a: number, b: number, c: number) => void;
  readonly __wbindgen_start: () => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;
/**
* Instantiates the given `module`, which can either be bytes or
* a precompiled `WebAssembly.Module`.
*
* @param {{ module: SyncInitInput }} module - Passing `SyncInitInput` directly is deprecated.
*
* @returns {InitOutput}
*/
export function initSync(module: { module: SyncInitInput } | SyncInitInput): InitOutput;

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {{ module_or_path: InitInput | Promise<InitInput> }} module_or_path - Passing `InitInput` directly is deprecated.
*
* @returns {Promise<InitOutput>}
*/
export default function __wbg_init (module_or_path?: { module_or_path: InitInput | Promise<InitInput> } | InitInput | Promise<InitInput>): Promise<InitOutput>;
