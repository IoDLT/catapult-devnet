rm -rf core-node/config/seed core-node/config/data
mkdir -p core-node/config/seed core-node/config/data
mkdir core-node/config/seed/00000

dd if=/dev/zero of=./core-node/config/seed/00000/hashes.dat bs=1 count=64
/opt/catapult/keccak/catapult.tools.nemgen -r core-node/config/ -p core-node/config/nemesis/public-test.properties 2> /tmp/nemgen.log

harvesting_mosaic_id=$(grep "cat.harvest" /tmp/nemgen.log | grep nonce  | awk -F=  '{split($0, a, / /); print a[9]}' | sort -u)
currency_mosaic_id=$(grep "cat.currency" /tmp/nemgen.log | grep nonce  | awk -F=  '{split($0, a, / /); print a[9]}' | sort -u)

echo Harvester: ${harvesting_mosaic_id}
echo Currency: ${currency_mosaic_id}

cp -r core-node/config/seed/* core-node/config/data/