# pulls release info from versions file

. ./versions

#

echo "making final tarball"
cd ./rpms/extract
tar -czvf ../../../../../amdocl-legacy-"$major"."$fedora".x86_64.tar.gz .


