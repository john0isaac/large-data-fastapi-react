/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";
export class FilesService {
    /**
     * Get Data Filenames
     * @returns string Successful Response
     * @throws ApiError
     */
    public static getDataFilenamesFilenamesGet(): CancelablePromise<Array<string>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/filenames"
        });
    }
}
