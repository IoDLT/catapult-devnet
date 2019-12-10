rm -rf seed data
mkdir -p seed data
mkdir seed/00000

dd if=/dev/zero of=./seed/00000/hashes.dat bs=1 count=64
/opt/catapult/catapult.tools.nemgen -r . -p ./nemesis/public-test.properties 2> /tmp/nemgen.log

harvesting_mosaic_id=$(grep "cat.harvest" /tmp/nemgen.log | grep nonce  | awk -F=  '{split($0, a, / /); print a[9]}' | sort -u)
currency_mosaic_id=$(grep "cat.currency" /tmp/nemgen.log | grep nonce  | awk -F=  '{split($0, a, / /); print a[9]}' | sort -u)

echo Harvester: ${harvesting_mosaic_id}
echo Currency: ${currency_mosaic_id}

cp -r seed/* data/