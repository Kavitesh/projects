class BloomFilter {
    constructor(size, hashCount) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new Array(size).fill(0);
    }

    _hashes(item) {
        let hashes = [];
        for (let i = 0; i < this.hashCount; i++) {
            let hash = this._murmurHash(item, i) % this.size;
            hashes.push(hash);
        }
        return hashes;
    }

    _murmurHash(key, seed) {
        let h = seed;
        for (let i = 0; i < key.length; i++) {
            h = Math.imul(h ^ key.charCodeAt(i), 0x5bd1e995);
            h ^= h >>> 15;
        }
        return Math.abs(h);
    }

    add(item) {
        this._hashes(item).forEach(hash => this.bitArray[hash] = 1);
    }

    check(item) {
        return this._hashes(item).every(hash => this.bitArray[hash] === 1);
    }
}

// Example Usage
const bf = new BloomFilter(1000, 5);

// Adding usernames
bf.add("player123");
bf.add("gamer_pro");

// Checking usernames
console.log(bf.check("player123"));  // true (probably exists)
console.log(bf.check("newbie42"));   // false (definitely not)
