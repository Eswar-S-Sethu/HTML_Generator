/* tslint:disable */
/* eslint-disable */
export function convert_columns(data_json: string, from_unit: string, to_unit: string, whole_num: any, roundoff: any): string;
export function compress_image(base64_input: string, quality: number, format: string): CompressedResult;
export function hash_file_bytes(data: Uint8Array, algo: string): string;
export function run_regex(pattern: string, text: string, flags: string): string;
export class CompressedResult {
  private constructor();
  free(): void;
  readonly bytes: Uint8Array;
  readonly format: string;
  readonly size_kb: number;
  readonly width: number;
  readonly height: number;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly convert_columns: (a: number, b: number, c: number, d: number, e: number, f: number, g: any, h: any) => [number, number];
  readonly __wbg_compressedresult_free: (a: number, b: number) => void;
  readonly compressedresult_bytes: (a: number) => [number, number];
  readonly compressedresult_format: (a: number) => [number, number];
  readonly compressedresult_size_kb: (a: number) => number;
  readonly compressedresult_width: (a: number) => number;
  readonly compressedresult_height: (a: number) => number;
  readonly compress_image: (a: number, b: number, c: number, d: number, e: number) => [number, number, number];
  readonly hash_file_bytes: (a: number, b: number, c: number, d: number) => [number, number];
  readonly run_regex: (a: number, b: number, c: number, d: number, e: number, f: number) => [number, number];
  readonly __wbindgen_export_0: WebAssembly.Table;
  readonly __wbindgen_malloc: (a: number, b: number) => number;
  readonly __wbindgen_realloc: (a: number, b: number, c: number, d: number) => number;
  readonly __wbindgen_free: (a: number, b: number, c: number) => void;
  readonly __externref_table_dealloc: (a: number) => void;
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
