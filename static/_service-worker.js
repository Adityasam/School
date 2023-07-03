
// Cache name
var CACHE_NAME = 'ARCH_CACHE';

// Files required to make this app work offline
var REQUIRED_FILES = [

];

self.addEventListener('install', function (event) {
    // Perform install step:  loading each required file into cache
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                // Add all offline dependencies to the cache
                return cache.addAll(REQUIRED_FILES);
            })
            .then(function () {
                return self.skipWaiting();
            })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(async function () {
        try {
            var res = await fetch(event.request);
            var cache = await caches.open(REQUIRED_FILES);
            //cache.put(event.request.url, res.clone());
            return res;
        }
        catch (error) {
            return caches.match(event.request);
        }
    }());
});

self.addEventListener('activate', function (event) {
    // Calling claim() to force a "controllerchange" event on navigator.serviceWorker
    event.waitUntil(self.clients.claim());
});