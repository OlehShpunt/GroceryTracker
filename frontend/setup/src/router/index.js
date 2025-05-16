import {createRouter, createWebHistory} from 'vue-router';

import ScanReceiptView from '../views/ScanReceiptView.vue';
import ScannedDataView from '../views/ScannedDataView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/scan-receipt',
            name: 'ScanReceipt',
            component: ScanReceiptView
        },
        {
            path: '/scanned-data',
            name: 'ScannedData',
            component: ScannedDataView
        }
    ]
});

export default router;