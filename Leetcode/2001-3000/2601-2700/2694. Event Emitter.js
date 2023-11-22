// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    maps = {}

    getMap(event) {
        if (!this.maps[event]) {
            this.maps[event] = [];
        }
        return this.maps[event];
    }

    subscribe(event, cb) {
        this.getMap(event).push(cb);

        return {
            unsubscribe: () => {
                const l = this.getMap(event);
                l.splice(l.indexOf(cb), 1);
            }
        };
    }

    emit(event, args = []) {
        return this.getMap(event).map(cb => cb(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */