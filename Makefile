
.PHONY: build test publish hack

build:
	sui move build

test:
	sui move test

publish:
	sui client publish --gas-budget 1000

hack:
	sui client call --function get_flag --module hack --package 0x3746837aed286d2f52cc5b79d9f2855d2b2078e2 --gas-budget 10000 --args 0x37199c8a9c83338e6bea3a30002eaa0eab510860