/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateResponse } from "../models/CreateResponse";
import type { Data } from "../models/Data";
import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";
export class DataService {
    /**
     * Get Data
     * @returns Data Successful Response
     * @throws ApiError
     */
    public static getDataDataGet(): CancelablePromise<Array<Data>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/data"
        });
    }
    /**
     * Populate Data
     * @param fileName
     * @returns CreateResponse Successful Response
     * @throws ApiError
     */
    public static populateDataDataPopulateFileNameGet(fileName: string): CancelablePromise<CreateResponse> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/data/populate/{file_name}",
            path: {
                file_name: fileName
            },
            errors: {
                422: `Validation Error`
            }
        });
    }
}
